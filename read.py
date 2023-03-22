import time
import re
import json

geo = "records/geo30000.txt"
per = "records/persona.txt"

# def parse_file(file_name: str):
#     with open(file_name, mode="r", encoding="utf-8", errors="ignore") as file:
#         data = file.read()
#         # data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=\w{1,}\n", data)[1:]
#     return data


# def tag_mapper(line: str):
#     if line.find("DOCUMENT") >= 0:
#             pass
#     elif line.find("FORM=") >= 0:
#         pass
#     else:
#         try:
#             tag, v = line.split("|", 1)
#             tag = tag[1:4]
#             if result.get(tag):
#                 result[tag].append(v)
#             else:
#                 result[tag] = [v]
#         except Exception:
#             pass
def parse_file(file_name: str):
    result = {} 
    file = open(file_name, mode="r", encoding="utf-8", errors="ignore")
    bne_id = None
    for line in file:
        if line.find("DOCUMENT") >= 0:
            pass
        elif line.find("FORM=") >= 0:
            pass
        else:
            try:
                is_tag = True if line[1:4].isdigit() else False
                if is_tag:
                    tag, v = line.split("|", 1)
                else:
                    result[tag].append({bne_id:v})
                    continue
                v = f"|{v}"
                tag = tag[1:4]
                if tag == "001":
                    bne_id = v[2:-1]
                    result[bne_id] = {tag:v}
                if result.get(bne_id):
                    result[bne_id][tag] = v
                if result.get(tag):
                    result[tag].append({bne_id:v})
                else:
                    result[tag] = [{bne_id:v}]
            except Exception:
                pass
    file.close()
    file = open("results/test.json", "w", encoding="utf-8")
    json.dump(result, file, indent=4)
    file.close()
    return result
    
start = time.perf_counter()
data = parse_file(per)


tag = "375"
ss = "mas"
ids = []
for pair in data.get(tag):
    k,v = tuple(*pair.items())
    if v.find(ss) >= 0:
        ids.append(k)
result = []
for v in ids:
    result.append(data.get(v))
# print(result)
finish = time.perf_counter()

print("-".center(50, "-"))
print(finish-start)