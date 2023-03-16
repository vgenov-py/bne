import json
import csv
import re
from qmo import QMO
from tqdm import tqdm
'''
Getting from author_370 |0 and querying geo_781
'''
result = {}
def get_data(file_name: str) -> tuple:
    with open(file_name, encoding="utf-8") as file:
        return json.load(file)["data"]
    
geo_data = get_data("geo30000.json")

geo_001_781 = {}
for record in geo_data:
    geo_001_781[record.get("001:")[2:]] = record.get("781:")

pers_data = get_data("370_0.json")
counter_changed = 0
counter = 0
for record in pers_data:
    '''
    \|0XX\d{6}
    '''
    geo_001 = re.findall("\|0XX\d{5,7}", record.get("370:"))
    try:
        geo_001 = geo_001[0][2:]
        result[record.get("001:")[2:]] = {"370:OLD":record.get("370:"),"370:NEW":geo_001_781[geo_001], "100": record.get("100:"), "670":record.get("670:")}
        counter_changed += 1
    except Exception:
        counter += 1
print(f"Registros cambiados: {counter_changed}")

with open("results/result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)