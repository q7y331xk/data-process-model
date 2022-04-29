from search_func.match_str import match_keywords

def extract_brand_model(models, processed_selling, default):
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