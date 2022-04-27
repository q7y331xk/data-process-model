from rds.rds import write
from search_func.match_str import match_keywords

def process_datum(selling_list, models):
    default = '.'
    processed_selling = selling_list
    brand = default
    model_name = default

    for model in models:
        if model["additional_keywords"]:
            keywords = [model["model_name"]] + model["additional_keywords"]
        else:
            keywords = [model["model_name"]]
        model_found = match_keywords(processed_selling[1].replace(' ',''), keywords, default)
        if model_found != default:
            brand = model["brand"]
            model_name = model["model_name"]

    processed_selling.append(brand)
    processed_selling.append(model_name)

    return processed_selling

def process_data(table, sellings_exist, models, start_id):
    for selling in sellings_exist:
        selling_list = list(selling)
        if (selling_list[0] <= start_id):
            continue
        processed_selling = process_datum(selling_list, models)
        print(processed_selling)
        write(table, processed_selling)
        print('done')