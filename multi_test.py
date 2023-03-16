import time
from marc_reader import parse_file
from multiprocessing import Pool, freeze_support
import re
from qmo import QMO
from utils import dict_mapper
geo = "records/geo30000.txt"
per = "records/persona.txt"
books_name = "records/monomodernas003.txt"
# data = parse_file(file_name)
# data = parse_file(books_name)

def parse_file(file_name: str):
    with open(file_name, mode="r", encoding="utf-8", errors="ignore") as file:
        data = file.read()
        data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=\w{1,}\n", data)[1:]
    return data
start = time.perf_counter()
data = parse_file(per)
finish = time.perf_counter()
print(finish - start)
start = time.perf_counter()
a = tuple(map( lambda record: dict_mapper(record), data))
print(a[2344])
finish = time.perf_counter()
print(finish - start)

# POOL:
# start = time.perf_counter()
# freeze_support()
# with Pool(processes=4) as pool:
#     results = pool.map(dict_mapper, data)
# finish = time.perf_counter()
# print(finish - start)

# if __name__ == "__main__":
#     start = time.perf_counter()
#     freeze_support()
#     with Pool(processes=4) as pool:
#         results = pool.map(dict_mapper, data)
#     finish = time.perf_counter()
#     print(finish - start)