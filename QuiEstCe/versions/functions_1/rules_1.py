from tkinter import *
from functions.destroy import *


def rules():

  background_color = "white"
  rules_window = Tk()
  rules_window.geometry("600x400")
  rules_window.title("   Régles - Qui Est-Ce ?")
  rules_window.overrideredirect(True)
  rules_window.resizable(False, False)
  rules_window.configure(background=background_color)

  rules_title_label = Label(rules_window, text="Régles du Jeu", font=("Arial",30), bg=background_color)
  rules_title_label.place(x=300,y=50,anchor=CENTER)
  
  rules_explanation_label = Label(rules_window, text="Bonjour ! Et bienvenue sur Qui Est Ce ? Le célébre jeu de déduction\n Voice les régles:", bg=background_color)
  rules_explanation_label.place(x=300,y=150,anchor=CENTER)

  rules_exit_button = Button(rules_window, text="Menu", font=("Arial",10),command=lambda *args: window_destroy(rules_window), bg=background_color)
  rules_exit_button.place(x=300,y=330,anchor=CENTER)