import re

def match_keywords(text, keywords, default=None):
    found = default
    for keyword in keywords:
        match = re.search(keyword.replace(' ',''),text)
        if match:
            found = match.group()
            break
    return found
