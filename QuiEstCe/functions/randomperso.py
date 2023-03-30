#_____Imported_functions_____#
import csv
from random import randint
from functions.play import *
#_____Global_values_____#
global answer
#_____Ramdomly_select_person_function_____#
def random_perso():
  global selected_person
  list_caractere = []
  with open("data/Guess_who_Nom.csv",newline="") as csvfile:
    caracteres = csv.DictReader(csvfile)
    for caractere in caracteres:
      list_caractere.append(caractere['Nom'])
  random_number = randint(0,len(list_caractere)-1)
  selected_person = list_caractere[random_number]
  return selected_person
#_____Respond_question_function_____#
def reponse(categorie, sub_categorie):
  global selected_person
  global answer
  answer = 'NON'
  list_nom = []
  with open(f"data/Guess_who_{categorie}.csv",newline="") as file:
    main_categorie = csv.DictReader(file)
    for sub in main_categorie:
      list_nom.append(sub[sub_categorie])
  if selected_person in list_nom:
    answer = 'OUI'
#_____Verify_player_guess_function____##
def verify_answer(name, selected_person):
  global status
  status = 'loser'
  if name == selected_person:
    status = 'winner'