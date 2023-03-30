#########################################################
##                     Main File                       ##
#########################################################

#------------------------Import-------------------------#
from tkinter import *
from PIL import ImageTk
import PIL.Image
import csv

from functions.rules import *
from functions.play import *
#------------------------Import-------------------------#

#PARAMETRE TKINTER:
master_root = Tk()
master_root.geometry("600x400")
master_root.title("        Qui Est-Ce ?")
master_root.overrideredirect(True)
master_root.resizable(False, False)
#master_root.iconbitmap("images/qui_est-ce?.jpeg")


#Parametre window principal:
background_color = "white" #white
font_color = "#124179" #blue
master_root.configure(background=background_color)



game_rules_button = Button(master_root, text="Régles", foreground=font_color,  background=background_color, font=("Arial",15),command=rules, bd=0, relief=FLAT, highlightcolor='red')
game_rules_button.place(x=200,y=330,anchor=CENTER)


play_button = Button(master_root, text="Jouer", foreground=font_color,  background=background_color, font=("Arial",15),command=play, bd=0, relief=FLAT)
play_button.place(x=400,y=330,anchor=CENTER)

qui_est_ce_image = PIL.Image.open("images/qui_est_ce.png")
resized_qui_est_ce = qui_est_ce_image.resize((300, 300))
qui_est_ce_resized = ImageTk.PhotoImage(resized_qui_est_ce)


logo_welcome_label = Label(master_root, image = qui_est_ce_resized, background=background_color)
logo_welcome_label.place(x=300, y=160, anchor=CENTER)




master_root.mainloop()
