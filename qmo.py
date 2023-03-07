import re
import csv
from utils import csv_mapper
class QMO:
    def __init__(self, data: tuple) -> None:
        self.data = data

    @property
    def length(self):
        return len(self.data)

    def without_tag(self, tag:str):
        result = []
        for record in self.data:
            if not record.get(f"{tag}:"):
                result.append(record)
        return tuple(result)
    
    def filter_by_tag(self, tag:str, search_str: str) -> tuple:
        result = []
        for record in self.data:
            for k, v in record.items():
                if k.startswith(f"{tag}:"):
                    if v.lower().find(search_str.lower()) >= 0:
                        result.append(record)
        return tuple(result)

    def export_csv(self, csv_name: str, data: tuple):
        HEADERS = "id BNE;otros códigos de identificación;coordenadas;cdu;encabezamiento geográfico;término geográfico no aceptado;entidades relacionadas;término de materia relacionado;término geográfico relacionado;término geográfico relacionado genérico;término geográfico relacionado específico;nota general;fuente de información;información encontrada;enlace a fuente;otros datos biográficos o históricos;nota de uso;geográfico subencabezamiento;obras relacionadas"
        HEADERS = HEADERS.split(";")
        with open(f"{csv_name}.csv", "w", encoding="utf-8") as file:
            def write_lines(data):
                to_write = []
                for record in data:
                    a = csv_mapper(record)
                    to_write.append(a)
                return to_write
            csv_writter = csv.writer(file, delimiter=";")
            csv_writter.writerow(HEADERS)
            b = write_lines(data)
            csv_writter.writerows(b)

if __name__ == "__main__":
    test = QMO(("a","b"))
