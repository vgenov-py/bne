from utils import dict_mapper
from qmo import QMO
from tqdm import tqdm
import re

def parse_file(file_name: str):
    with open(file_name, mode="r", encoding="utf-8") as file:
        data = file.read()
        if file_name.find("geo") >= 0:
            data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=GEOGRAFICO\n", data)[1:]
        elif file_name.find("per") >= 0:
            data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=PERSONA\n", data)[1:]
        elif file_name.find("sono") >= 0:
            data = re.split("\*\*\* DOCUMENT BOUNDARY \*\*\*\nFORM=GRABSONORA\n", data)[1:]
        data = tuple(map(lambda record: dict_mapper(record), tqdm(data)))
    return QMO(data, file_name.split("/")[-1])

if __name__ == "__main__":
    import os
    test = parse_file(f"{os.getcwd()}/records/geo30000.txt")
    print(test.data[5000])