import re

re_tag = "\.\d{3}\.\W{1,3}\||\.\d{3}\.\W{1}\d{1,2}\W{1}\||\.\d{3}\.\d{1,2}\W{1,2}\|"
re_dollar = "\|.{1}"
'''
DEPRECATED SINCE 8-3-2023:
'''
# def dollar_parser(subfields: str) -> tuple:
#     '''
#     |a2010|22020 -> 2010 2020
#     Every string should be in explicit-mode (starting with |)
#     '''
#     for i, text in enumerate(subfields[5:]):
#         dollars = re.findall(re_dollar, text)
#         dollars = map(lambda dollar: dollar.replace("|", ""), dollars)
#         dollar_texts = re.split(re_dollar, text)[1:]
#         subfields[i + 5] = tuple(zip(dollars, dollar_texts))

'''
DEPRECATED SINCE 7-3-2023:
'''

# def dict_mapper(record: str) -> dict:
#     tags = list(map(lambda tag: f"{tag[1:4]}:", re.findall(re_tag, record)))
#     tag_coincidence = 0
#     for i, tag in enumerate(tags):
#         if tags[i-1][0:4] == tag:
#             tag_coincidence += 1
#             tags[i] += f"{tag_coincidence}"
#         else:
#             tag_coincidence = 0

#     texts = re.split(re_tag, record)[1:]
#     texts = map(lambda text:f"|{text}", texts)
#     # texts = map(lambda text:text.replace("\n",""), texts)
#     result = dict(zip(tags,texts))
#     return result

def dict_mapper(record: str) -> dict:
    result = {}
    tag_coincidence = 0
    old_tag = None
    for line in re.split("\n(?=\.\d{3}\.)", record):
        tag, value = line.split("|", 1)
        tag = f"{tag[1:4]}:"
        if old_tag == tag:
            tag_coincidence += 1
            tag = f"{tag[0:3]}:{tag_coincidence}"
        else:
            tag_coincidence = 0
        result[tag] = f"|{value}"
        old_tag = tag
    return result

def dollar_replacer(subfield: str, replacer:str = " "):
    '''
    |a2010|22020 -> 2010 2020
    Every string should be in explicit-mode (starting with |)
    '''
    try:
        return re.sub(re_dollar, replacer, subfield).strip()
    except TypeError:
        return subfield

def csv_mapper(record: dict) -> tuple:
    '''
    This function will take a dict as an argument and will return the current expected fields to fill the geographic csv
    tags considered: 001, 024, 034... 
    '''
    bne_id = record.get("001:").replace("\n", "") if record.get("001:") else None
    bne_id = dollar_replacer(bne_id)

    '''
    024
    '''
    other_codes = ""
    for k, v in filter(lambda k: k[0].startswith("024"), record.items()):
        other_codes += f"{dollar_replacer(v)} ** "

    coord = record.get("034:").replace("\n", "") if record.get("034:") else None
    coord = dollar_replacer(coord)
    cdu = record.get("080:").replace("\n", "") if record.get("080:") else None
    cdu = dollar_replacer(cdu)
    header_geo = record.get("151:").replace("\n", "") if record.get("151:") else None
    header_geo = dollar_replacer(header_geo)
    '''
    451
    '''
    not_accepted_term = ""
    for k, v in filter(lambda k: k[0].startswith("451"), record.items()):
        other_codes += f"{dollar_replacer(v)} "
    related_geo_term = record.get("550:").replace("\n", "") if record.get("550:") else None
    related_geo_term = dollar_replacer(related_geo_term)
    return tuple([bne_id, other_codes, coord, cdu, header_geo, not_accepted_term, related_geo_term])

if __name__ == "__main__":
    pass