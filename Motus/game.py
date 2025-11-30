# Codé en utf 8



import csv
from random import choice


l = []
with open("mots.csv", mode = "r") as fichier:
    reader = csv.reader(fichier)
    for i in reader :
        l.append(i)

     
mot = choice(l)



        