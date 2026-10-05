"""
Ex. 1. Scrieţi un program în Python care să preia ca input un fişier .csv cu o listă oarecare şi să aibă ca output un număr
predeterminat de elemente din acea listă, fără repetiţie. Aplicaţi pe lista studenţilor din grupa dumneavoastră care nu
au prezentat încă o temă.
"""
import csv
import random

nume_fisier = input("Numele fisierului:")
n = int(input("Numarul de elemente:"))

lista = []
with open(nume_fisier, "r") as f:
    reader = csv.reader(f)
    for line in reader:
        if line:
            lista.append(line[0])

if n > len(lista):
    print("prea multe elemente")
else:
    rand = random.sample(lista, n)
    for name in rand:
        print(name)
