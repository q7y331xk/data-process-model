from cmath import log
import re
from unittest import case
from search_func.match_str import match_keywords

def extract_status(keywords_status, processed_selling):
    title = processed_selling[1]
    for keyword in keywords_status:
        found = re.search(keyword["key"], title)
        if found:
            processed_selling[4] = keyword["value"]

def extract_brand_model(models, processed_selling, default=None):
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

def extract_cnt(keywords_cnt, processed_selling):
    title = processed_selling[1]
    condition = processed_selling[6]
    body = processed_selling[10]
    
    found_in_condition = re.search("미개봉", condition)
    if found_in_condition:
        processed_selling[5] = "0"
        return

    found_in_title = re.search("신품", title)
    if found_in_title:
        processed_selling[5] = "0"
        return 
    found_in_title = re.search("양도", title)
    if found_in_title:
        processed_selling[5] = "0"
        return

    found_hoe = re.search(r"[0-9]+회", body)
    if found_hoe:
        processed_selling[5] = found_hoe.group().replace('회', '')
        return
    found_bun = re.search(r"[0-9]+번", body)
    if found_bun:
        processed_selling[5] = found_bun.group().replace('번', '')
        return
    
    for keyword in keywords_cnt:
        found = re.search(keyword["key"], body)
        if found:
            processed_selling[5] = keyword["value"]
            return

def extract_grade(processed_selling):
    cnt = int(processed_selling[5])
    grade = "U"
    if processed_selling[21] == 1:
        grade = "F"
    elif cnt == -1:
        grade = "U"
    elif cnt == 0:
        grade = "A"
    elif (cnt == 1 or cnt == 2):
        grade = "B"
    elif (cnt == 3 or cnt == 4 or cnt == 5):
        grade = "C"
    elif cnt > 5:
        grade = "D"
    else:
        grade = "Err"
    processed_selling.append(grade)

def extract_jangbak(processed_selling, default):
    jangbak = default
    body = processed_selling[10]
    body_converted = body.replace(' ', '').upper().replace('포장박스', '').replace('장박용', '').replace('장박없', '').replace('장박X', '').replace('장박이력없', '')
    found = re.search('장박', body_converted)
    if found:
        jangbak = 1
    processed_selling.append(jangbak)

def extract_limited(keywords_limited, processed_selling):
    title = processed_selling[1]
    limited = 0
    for keyword in keywords_limited:
        found = re.search(keyword["key"], title)
        if found:
            limited = 1
            break
    processed_selling.append(limited)

def extract_groundsheet(keywords_groundsheet, processed_selling):
    title = processed_selling[1]
    body = processed_selling[10]
    groundsheet = 0
    for keyword in keywords_groundsheet:
        found = re.search(keyword["key"], title.replace(" ",""))
        if found:
            groundsheet = 1
            processed_selling.append(groundsheet)
            return
    for keyword in keywords_groundsheet:
        found = re.search(keyword["key"], body.replace(" ",""))
        if found:
            groundsheet = 1
    processed_selling.append(groundsheet)

def extract_inner_tent(keywords_inner_tent, processed_selling):
    title = processed_selling[1]
    body = processed_selling[10]
    inner_tent = 0
    for keyword in keywords_inner_tent:
        found = re.search(keyword["key"], title.replace(" ","").replace("라이너","").replace("이너매트","").replace("이너메트",""))
        if found:
            inner_tent = 1
            processed_selling.append(inner_tent)
            return
    for keyword in keywords_inner_tent:
        found = re.search(keyword["key"], body.replace(" ","").replace("라이너","").replace("이너매트","").replace("이너메트",""))
        if found:
            inner_tent = 1
    processed_selling.append(inner_tent)

def extract_set(keywords_set, processed_selling):
    set = 0
    if processed_selling[24] or processed_selling[25] or processed_selling[26] or processed_selling[27]:
        set = 1
        processed_selling.append(set)
        return
    else:
        title = processed_selling[1]
        for keyword in keywords_set:
            found = re.search(keyword["key"], title.replace(',0',''))
            if found:
                set = 1
                processed_selling.append(set)
                return    
        body = processed_selling[10]
        found = re.search("2.", body.replace('2.0',''))
        if found:
            set = 1            
    processed_selling.append(set)
    
def extract_urethane(keywords_urethane, processed_selling):
    title = processed_selling[1]
    body = processed_selling[10]
    urethane = 0
    for keyword in keywords_urethane:
        found = re.search(keyword["key"], title)
        if found:
            urethane = 1
            processed_selling.append(urethane)
            return
    for keyword in keywords_urethane:
        found = re.search(keyword["key"], body)
        if found:
            urethane = 1
    processed_selling.append(urethane)

def extract_vestibule(keywords_vestibule, processed_selling):
    title = processed_selling[1]
    body = processed_selling[10]
    vestibule = 0
    for keyword in keywords_vestibule:
        found = re.search(keyword["key"], title)
        if found:
            vestibule = 1
            processed_selling.append(vestibule)
            return
    for keyword in keywords_vestibule:
        found = re.search(keyword["key"], body)
        if found:
            vestibule = 1
    processed_selling.append(vestibule)
    