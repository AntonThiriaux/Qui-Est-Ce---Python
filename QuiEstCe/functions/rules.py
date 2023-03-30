#_____Imported_function_____#
from tkinter import *
from functions.destroy import *
#_____Rules_explanation_function_____#
def rules():
  #_____Window_parameters_____#
  rules_window = Tk()
  rules_window.geometry("650x420")
  rules_window.title("   Règles - Qui Est-Ce ?")
  rules_window.overrideredirect(True)
  rules_window.resizable(False, False)
  background_color = "white"
  rules_window.configure(background=background_color)
  font_color = "#124179" #blue
  #_____Widgets_defining_____#
  #lb_rules_title#
  lb_rules_title = Label(rules_window, text="Règles du Jeu", font=("Arial",30), bg=background_color, fg=font_color)
  lb_rules_title.place(x=300,y=50,anchor=CENTER)
  #lb_rules_explanation#
  lb_rules_explanation = Label(rules_window, text="Bonjour ! Et bienvenue sur Qui Est-Ce ?\nLe célèbre jeu de déduction.\n Voici les règles:", bg=background_color, fg=font_color, font=('arial', 13))
  lb_rules_explanation.place(x=300,y=115,anchor=CENTER)
  #btn_rules_quit#
  btn_rules_quit = Button(rules_window, text="     Menu    ", font=("Arial",10),command=lambda *args: window_destroy(rules_window), bg=background_color, fg=font_color, activeforeground=font_color, relief=FLAT)
  btn_rules_quit.place(x=300,y=390,anchor=CENTER)
  #lb_rules#
  lb_rules = Label(rules_window, text="24 images avec des personnages s'afficheront. L'ordinateur va choisir un\npersonnage et votre but est de le trouver avec le score le plus petit possible.\nPour ce faire, vous disposez de questions préprogrammées au-dessous.\nÀ chaque question posée, ou à chaque fois que vous devinez un personnage,\nvotre score augmente de 1.\nSi vous voulez cacher une image faites:\n- clique gauche ou double clique gauche\nSi vous voulez la faire réapparaître faites:\n- clique gauche ou double clique gauche\nSi vous voulez agrandir une image faites:\n- clique droit\nEnfin si vous pensez avoir trouvé le personnage:\n- appuyez sur le bouton en bas à droite pour deviner", bg='white', fg=font_color, font=('arial', 10, 'italic'), justify=LEFT)
  lb_rules.place(x=325, y=260, anchor=CENTER)