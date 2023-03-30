def verify_answer(name, selected_person):
  global status
  status = 'loser'
  if name == selected_person:
    status = 'winner'
  return status

assert verify_answer("Max", "Max") == "winner", "Erreur Fonction 'verify_answer' - deux bons"
print('\033[92m' + "Fonction 'verify_answer' --- ✔")
assert verify_answer("Max", "Georgia") == "winner", "Erreur Fonction 'verify_answer' - deux bons"
print('\033[92m' + "Fonction 'verify_answer' --- ✔")

assert reponse(f"{categorie}", f"{sous_cat}") == "NON", 