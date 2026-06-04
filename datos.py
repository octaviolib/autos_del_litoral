import json
import os

ARCHIVO = "autos.txt"

def cargar_datos():

    if not os.path.exists(ARCHIVO):
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except:
        return []

def guardar_datos(autos):

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(autos, archivo, indent=4)
