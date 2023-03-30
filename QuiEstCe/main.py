#_____Imported_functions#
from tkinter import *
from PIL import ImageTk
import PIL.Image
import csv
from functions.rules import *
from functions.play import *
from functions.randomperso import *
#_____Window_parameters_____#
master_root = Tk()
master_root.geometry("650x420")
master_root.title("        Qui Est-Ce ?")
master_root.overrideredirect(True)
master_root.resizable(False, False)
background_color = "white" #white
font_color = "#124179" #blue
master_root.configure(background=background_color)
#_____Image_resizing_____#
qui_est_ce_image = PIL.Image.open("images/qui_est_ce.png")
resized_qui_est_ce = qui_est_ce_image.resize((300, 300))
qui_est_ce_resized = ImageTk.PhotoImage(resized_qui_est_ce)
#_____Widgets_defining_____#
#btn_game_rules#
btn_game_rules = Button(master_root, text="     Règles     ", foreground=font_color,  background=background_color, font=("Arial",15),command=rules, bd=0, relief=FLAT, highlightcolor='red', activeforeground=font_color)
btn_game_rules.place(x=225,y=340,anchor=CENTER)
#btn_play#
btn_play = Button(master_root, text="     Jouer     ", foreground=font_color,  background=background_color, font=("Arial",15),command=lambda: [play(), random_perso()], bd=0, relief=FLAT, activeforeground=font_color)
btn_play.place(x=425,y=340,anchor=CENTER)
#lb_welcome#
lb_welcome = Label(master_root, image = qui_est_ce_resized, background=background_color)
lb_welcome.place(x=325, y=170, anchor=CENTER)
#_____Mainloop_____#
master_root.mainloop()