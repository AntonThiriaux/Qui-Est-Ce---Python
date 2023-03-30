import csv

def questions():
  with open("Qui.csv",newline="") as csvfile:
    persons = csv.DictReader(csvfile)
    print(persons)
      
      