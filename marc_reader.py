import time
from utils import dict_mapper
from qmo import QMO
from tqdm import tqdm
import re
import os


start = time.perf_counter()
def parse_file(file_name: str):
    with open(file_name, mode="r", encoding="utf-8") as file:
        data = file.read()
        if file_name.startswith(f"{os.getcwd()}/records/geo"):
            data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=GEOGRAFICO\n", data)[1:]
        else:
            data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=PERSONA\n", data)[1:]
        data = tuple(map(lambda record: dict_mapper(record), tqdm(data)))
    return QMO(data)


'''
csv converter:
'''
# test.export_csv("persona", data)
finish = time.perf_counter()
# print("-".center(100,"-"))
# print(finish-start)