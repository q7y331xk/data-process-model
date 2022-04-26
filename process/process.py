from rds.rds import write
from search_func.match_str import match_keywords

def process_datum(selling, models):
    default = '.'
    processed_selling = list(selling)
    brand = default
    model_name = default

    for model in models:
        if model["additional_keywords"]:
            keywords = [model["model_name"]] + model["additional_keywords"]
        else:
            keywords = [model["model_name"]]
        model_found = match_keywords(selling[1].replace(' ',''), keywords, default)
        if model_found != default:
            brand = model["brand"]
            model_name = model["model_name"]

    processed_selling.append(brand)
    processed_selling.append(model_name)
    return processed_selling

def process_data(table, sellings_exist, models):
    for selling in sellings_exist:
        processed_selling = process_datum(selling, models)
        write(table, processed_selling)