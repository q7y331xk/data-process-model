from process.process_sub import extract_brand_model, extract_inner_tent, extract_jangbak, extract_status, extract_cnt, extract_grade, extract_limited, extract_groundsheet, extract_set, extract_vestibule, extract_urethane
from rds.rds import write
from search_func.match_str import match_keywords
from search_data.status import keywords_status
from search_data.cnt import keywords_cnt
from search_data.limited import keywords_limited
from search_data.components import keywords_groundsheet, keywords_inner_tent, keywords_set, keywords_urethane, keywords_vestibule

def process_datum(selling_list, models):
    default = '.'
    processed_selling = selling_list
    extract_status(keywords_status, processed_selling)
    extract_cnt(keywords_cnt, processed_selling)
    extract_brand_model(models, processed_selling, default)
    extract_jangbak(processed_selling, 0)
    extract_grade(processed_selling)
    extract_limited(keywords_limited, processed_selling)
    extract_groundsheet(keywords_groundsheet, processed_selling)
    extract_inner_tent(keywords_inner_tent, processed_selling)
    extract_urethane(keywords_urethane, processed_selling)
    extract_vestibule(keywords_vestibule, processed_selling)
    extract_set(keywords_set, processed_selling)
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