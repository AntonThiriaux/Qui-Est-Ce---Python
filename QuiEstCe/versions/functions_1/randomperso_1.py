import csv
from random import randint

def random_perso():
  list_caractere = []
  with open("data/Guess_who_name.csv",newline="") as csvfile:
    caracteres = csv.DictReader(csvfile)
    for caractere in caracteres:
      list_caractere.append(caractere['Nom'])
  random_number = randint(0,len(list_caractere)-1)
  caractere = list_caractere[random_number]
  return caractere
print(random_perso())