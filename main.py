import os
from marc_reader import parse_file
import random
from qmo import QMO
'''
'|cEspaña|eAndalucía, Cádiz (Provincia), Jerez de la Frontera'
|aAparicio, Francisco|d1915-1997
'''

RECORDS_DIR = f"{os.getcwd()}/records"
sets = []
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")

def sub_menu(options: list) -> None:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

def menu():
    clear()
    options = ["Cargar ficheros/s", "MARC Query", "Consulta general","Exportar" , "Salir (Q)"]
    sub_menu(options)

def list_files(dir: str) -> None:
    files = os.listdir(dir)
    sub_menu(files)
    return files

def tag_value_query(tag: str, search_str: str, qmo_set: QMO) -> tuple:
    sub_set = qmo_set.filter_by_tag(tag, search_str)
    user = ""
    while user != "n": # DRY WET
        try:
            print(sub_set[random.randint(0,len(sub_set))])
            print(len(sub_set))
        except IndexError:
            print("SIN EJEMPLO")
        print("Seguir consultando (s/n)")
        user = input(": ")
        if user != "n":
            clear()
            sub_set = QMO(sub_set)
            tag = input("tag: ") # len == 0
            search_str = input("Buscar: ")
            sub_set = sub_set.filter_by_tag(tag, search_str)
            print("EJEMPLO:")
    return sub_set

user = ""

while user != "q":
    menu()

    if user == "1":
        clear()
        records = list_files(RECORDS_DIR)
        user = int(input(": ")) -1
        test = parse_file(f"{os.getcwd()}/records/{records[user]}")
        sets.append(test)
        clear()
        print(f"{records[user]} cargado correctamente\n")
        print("Ficheros cargados:")
        sub_menu(sets)
    elif user == "2":
        clear()
        sub_menu(("Filtrar por tag", "Filtrar por valor", "Multi-consulta"))
        user = input(": ")
        if user == "1":
            clear()
            tag = input("tag: ")
            result = test.without_tag(tag)
            print(len(result))
            print("1. Export CSV")
            user = input("(s/n): ")
            if user.lower() == "s":
                csv_name = input("Nombre del fichero: ")
                test.export_csv(csv_name, result)
        elif user == "2":
            clear()
            tag = input("tag: ")
            search_str = input("Buscar: ")
            result = tag_value_query(tag, search_str, test)
            print("1. Export CSV (s/n)")
            user = input("(s/n): ")
            if user.lower() == "s":
                csv_name = input("Nombre del fichero: ")
                test.export_csv(csv_name, result)
                QMO(result).export_json(csv_name)
        elif user == "3":
            clear()
            # 1. set query
            print("Elegir query set")
            sub_menu(sets)
            query_set = int(input(": ")) - 1
            query_set = sets[query_set]
            print(f"Query set: {query_set}")
            # 2. set reply
            print("Elegir reply set")
            sub_menu(sets)
            reply_set = int(input(": ")) - 1
            reply_set = sets[reply_set]
            print(f"Reply set: {reply_set}")
            # 3. generate sub query set
            clear()
            print("Filtrar query set")
            tag = input("tag: ")
            search_str = input("Buscar: ")
            query_set = tag_value_query(tag, search_str, query_set)
            # 4. select query tag
            clear()
            print("Seleccionar tag del query set a encontrar en el reply set")
            query_tag = input(": ")
            query_values = QMO(query_set).query_tags(query_tag)
            print(query_values)
            input(": ")
            # 5. select match tag
            clear()
            print("Seleccionar match tag")
            print("Match tag será la etiqueta donde serán consultados los valores generados en el paso anterior")
            match_tag = input(": ")
            reply_set = reply_set.filter_by_values(match_tag, query_values)
            print(reply_set)
            # 6. export json
            clear()
            print("¿Exportar en json (s/n)?")
            user = input(": ")
            if user.lower() == "s":
                file_name = input("Nombre del fichero: ")
                reply_set = QMO(reply_set)
                reply_set.export_json(file_name)
    elif user == "4":
        sub_menu(("JSON", "CSV"))
        user = input(": ")
        if user == "1":
            file_name = input("Nombre del fichero: ")
            test.export_json(file_name)


    user = input(": ")