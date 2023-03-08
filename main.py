import os
from marc_reader import parse_file
RECORDS_DIR = f"{os.getcwd()}/records"
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")
def menu():
    clear()
    options = ["Cargar ficheros/s", "MARC Query", "Consulta general", "Salir"]
    for i, option in enumerate(options[0:-1]):
        print(f"{i+1}. {option}")
def sub_menu(options: list) -> None:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
def list_files(dir: str) -> None:
    files = os.listdir(dir)
    sub_menu(files)
    return files
user = ""
while user != "q":
    menu()

    if user == "1":
        pass
        records = list_files(RECORDS_DIR)
        user = int(input(": ")) -1
        test = parse_file(f"{os.getcwd()}/records/{records[user]}")
        clear()
        print(f"{records[user]} cargado correctamente")
        input()
    elif user == "2":
        sub_menu(("Filtrar por tag", "Filtrar por valor"))
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