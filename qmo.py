import re
import csv
from utils import csv_mapper

class QMO:
    def __init__(self, data: tuple, file_name=None) -> None:
        self.data = data
        self.file_name = file_name
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
    
    def query_tags(self, query_tag: str) -> tuple:
        '''
        This function will return a tuple of all the values asociated to the query tag
        '''
        def get_values_by_tag():
            for record in self.data:
                value = record.get(f"{query_tag}:")
                if value:
                    yield value
        return tuple(get_values_by_tag())
    
    def filter_by_values(self, match_tag: str, values: tuple) -> tuple:
        result = []
        for record in self.data:
            reply_value = record.get(f"{match_tag}:")
            if len(tuple(filter(lambda value: value in reply_value, values))):
                result.append(record)
        return tuple(result)

    def export_csv(self, csv_name: str, data: tuple):
        HEADERS = ['id BNE', 'otros códigos de identificación', 'coordenadas', 'cdu', 'encabezamiento geográfico', 'término geográfico no aceptado', 'entidades relacionadas', 'término de materia relacionado', 'término geográfico relacionado', 'término geográfico relacionado genérico', 'término geográfico relacionado específico', 'nota general', 'fuente de información', 'información encontrada', 'enlace a fuente', 'otros datos biográficos o históricos', 'nota de uso', 'geográfico subencabezamiento', 'obras relacionadas']
        with open(f"{csv_name}.csv", "w", encoding="utf-8") as file:
            def write_lines(data):
                for record in data:
                    yield csv_mapper(record)
            csv_writter = csv.writer(file, delimiter=";")
            csv_writter.writerow(HEADERS)
            b = write_lines(data)
            csv_writter.writerows(b)

    def __str__(self):
        return f"{self.file_name}"
    def __repr__(self):
        return f"{self.file_name}"
    
if __name__ == "__main__":
    test = QMO(("a","b"))
