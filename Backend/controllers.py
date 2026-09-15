import json


def loads_menu():
    with open("Menu.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def create_menu():
    print("lom ada")

def update_menu():
    print("ksabar")