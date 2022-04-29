from process.process_sub import extract_brand_model
from rds.rds import write
from search_func.match_str import match_keywords

def process_datum(selling_list, models):
    default = '.'
    processed_selling = selling_list
    extract_brand_model(models, processed_selling, default)
    return processed_selling

def process_data(sellings_exist, models, skip_id):
    sellings_processed = []
    lows_cnt = len(sellings_exist)
    print(f"lows_cnt: {lows_cnt}")
    for selling in sellings_exist:
        selling_list = list(selling)
        if (selling_list[0] <= skip_id):
            continue
        processed_selling = process_datum(selling_list, models)
        sellings_processed.append(processed_selling)
        print(f"{selling[0]}/{lows_cnt}")
    return sellings_processed