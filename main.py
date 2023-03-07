import os
from marc_reader import test
import random
# import xmltodict
# with open('sub_geo.xml', 'r', encoding='utf-8') as file:
#     my_xml = file.read()

# data = xmltodict.parse(my_xml)
# print(data)

user = ""
while user != "q":
    os.system("clear")
    print("1. MARC Query")
    print("2. Consulta general")
    print("Q. Salir")
    print(f"{test.length} REGISTROS")

    if user == "1":
        print("1. Filtrar por tag")
        print("2. Filtrar por valor")
        user = input(": ")
        if user == "1":
            os.system("clear")
            tag = input("tag: ")
            result = test.without_tag(tag)
            print(len(result))
            print("1. Export CSV")
            user = input("(s/n): ")
            if user.lower() == "s":
                csv_name = input("Nombre del fichero: ")
                test.export_csv(csv_name, result)
        elif user == "2":
            os.system("clear")
            tag = input("tag: ")
            search_str = input("Buscar: ")
            result = test.filter_by_tag(tag, search_str)
            print(len(result))
            print("1. Export CSV (s/n)")
            user = input("(s/n): ")
            if user.lower() == "s":
                csv_name = input("Nombre del fichero: ")
                test.export_csv(csv_name, result)
    user = input(": ")