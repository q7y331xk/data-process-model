import re

def match_keywords(text, keywords, default=None):
    found = default
    for keyword in keywords:
        match = re.search(keyword.replace(' ',''),text)
        if match:
            found = match.group()
            break
    return found

# print(match_keywords("캠핑 용품 일괄정리",["용품","일괄"],'Not Found'))
# print(match_keywords("캠핑 용품 일괄정리",["용품","괴핑"],'Not Found'))
# print(match_keywords("캠핑 용품 일괄정리",["갑상선"],'Not Found'))
