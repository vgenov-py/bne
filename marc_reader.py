import time
from utils import dict_mapper
from qmo import QMO
import csv
import os
from tqdm import tqdm
import re


start = time.perf_counter()
file_name = "persona.txt"
with open(file_name, mode="r", encoding="utf-8") as file:
    data = file.read()
#     data = data.split('''
# *** DOCUMENT BOUNDARY ***
# FORM=GEOGRAFICO
# ''')
                      
    data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=PERSONA\n", data)[1:]
    data = tuple(map(lambda record: dict_mapper(record), tqdm(data)))
    print(data[1000])
test = QMO(data)

'''
csv converter:
'''
# test.export_csv("persona", data)
finish = time.perf_counter()
print("-".center(100,"-"))
print(finish-start)