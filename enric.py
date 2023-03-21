import json
import csv
import re
from qmo import QMO
from tqdm import tqdm
'''
Getting from author_370 |0 and querying geo_781
'''
result = {}
def get_data(file_name: str, is_list=False) -> tuple:
    with open(file_name, encoding="utf-8") as file:
        if is_list:
            return json.load(file)
        return json.load(file)["data"]
    
wiki_data = get_data("records/wiki_001_001.json", True)
wiki = map(lambda record: record.get("idlugar"), wiki_data)
per = get_data("results/per_wiki_001_001.json")
# geo = QMO(get_data("geo30000.json"))
# geo_781s = geo.filter_by_values("001",tuple(wiki))
# dict_geo_781s = {}
# for v in geo_781s:
#     dict_geo_781s[v.get("001:")[2:]]=v.get("781:")
# geo_781s = dict_geo_781s
# # geo_781s = map(lambda record: {record.get("001:"):record.get("781:")}, geo_781s)
# result = {}
# print("-".center(50, "-"))
# for value in tqdm(wiki_data):
#     id_per = value.get("idpersona")
#     id_place = value.get("idlugar")
#     place = geo_781s.get(id_place)
#     if place:
#         place = place.replace("|z", "|a", 1)
#         place = place.replace("|z", ", ")
#         result[id_per] = place
# print(result)

# with open("results/wiki_781s.json", "w", encoding="utf-8") as file:
#     json.dump(result, file, indent=4, ensure_ascii=False)
result = {}
wiki_781s = get_data("results/wiki_781s.json", True)
for record in per:
    per_id = record.get("001:")[2:]
    result[per_id] = {"370:OLD":record.get("370:"), "370:NEW": wiki_781s.get(per_id), "100:": record.get("100:"), "670": record.get("670:")}

with open("results/result_370_0_wiki.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

# print(per_geo)
# geo_001_781 = {}
# for record in geo_data:
#     geo_001_781[record.get("001:")[2:]] = record.get("781:")

result = {}
counter_changed = 0
counter = 0
for record in per:
    pass


# pers_data = per
# counter_changed = 0
# counter = 0
# for record in pers_data:
#     '''
#     \|0XX\d{6}
#     '''
#     geo_001 = re.findall("\|0XX\d{5,7}", record.get("370:"))
#     try:
#         geo_001 = geo_001[0][2:]
#         result[record.get("001:")[2:]] = {"370:OLD":record.get("370:"),"370:NEW":geo_001_781[geo_001], "100": record.get("100:"), "670":record.get("670:")}
#         counter_changed += 1
#     except Exception:
#         counter += 1
# print(f"Registros cambiados: {counter_changed}")

# with open("results/result.json", "w", encoding="utf-8") as file:
#     json.dump(result, file, indent=4, ensure_ascii=False)