#_____Import_functions_____#
from tkinter import *
from PIL import ImageTk
import PIL.Image
from random import randint
from functions.destroy import *
from functions.randomperso import *
import functions.randomperso
#_____Play_function_____#
def play():
 #_____Global_values_____#
  global optionmenu_update
  global image_baisse
  global load_label
  global under_categories
  global lb_zoom
  global score
  global history
  global nb_click_btn_try
  #_____Window_parameters_____#
  play_root = Toplevel()
  play_root.geometry("752x600")
  play_root.title("        Qui Est-Ce ?")
  play_root.overrideredirect(True)
  play_root.resizable(False, False)
  background_color = "white"  #white
  font_color = "#124179"  #blue
  play_root.configure(background=background_color)
  #_____Values_____#
  image_baisse = 0 
  score = 0
  nb_click_btn_try = 0
  optionmenu_update = False
  history = ''
  #Update#
  print('0%')
  #_____Images_resizing_____#
  n = 0
  for i in range(24):
    img = PIL.Image.open(f"images/peoples/Guess_who_{i}.png")
    resized_img = img.resize((70, 100))
    resized_img_zoom = img.resize((140, 200))
    img_text = PIL.Image.open(f"images/names/Guess_who_{i}_text.png")
    resized_img_text = img_text.resize((70, 40))
    n += 4
    if i == 0:
      print(n)
      andre = ImageTk.PhotoImage(resized_img)
      andre_text = ImageTk.PhotoImage(resized_img_text)
      andre_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 1:
      print(n)
      ayan = ImageTk.PhotoImage(resized_img)
      ayan_text = ImageTk.PhotoImage(resized_img_text)
      ayan_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 2:
      print(n)
      chris = ImageTk.PhotoImage(resized_img)
      chris_text = ImageTk.PhotoImage(resized_img_text)
      chris_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 3:
      print(n)
      daniel = ImageTk.PhotoImage(resized_img)
      daniel_text = ImageTk.PhotoImage(resized_img_text)
      daniel_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 4:
      print(n)
      eva = ImageTk.PhotoImage(resized_img)
      eva_text = ImageTk.PhotoImage(resized_img_text)
      eva_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 5:
      print(n)
      fred = ImageTk.PhotoImage(resized_img)
      fred_text = ImageTk.PhotoImage(resized_img_text)
      fred_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 6:
      print(n)
      george = ImageTk.PhotoImage(resized_img)
      george_text = ImageTk.PhotoImage(resized_img_text)
      george_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 7:
      print(n)
      georgia = ImageTk.PhotoImage(resized_img)
      georgia_text = ImageTk.PhotoImage(resized_img_text)
      georgia_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 8:
      print(n)
      greg = ImageTk.PhotoImage(resized_img)
      greg_text = ImageTk.PhotoImage(resized_img_text)
      greg_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 9:
      print(n)
      harriet = ImageTk.PhotoImage(resized_img)
      harriet_text = ImageTk.PhotoImage(resized_img_text)
      harriet_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 10:
      print(n)
      isobel = ImageTk.PhotoImage(resized_img)
      isobel_text = ImageTk.PhotoImage(resized_img_text)
      isobel_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 11:
      print(n)
      jayden = ImageTk.PhotoImage(resized_img)
      jayden_text = ImageTk.PhotoImage(resized_img_text)
      jayden_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 12:
      print(n)
      jess = ImageTk.PhotoImage(resized_img)
      jess_text = ImageTk.PhotoImage(resized_img_text)
      jess_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 13:
      print(n)
      leo = ImageTk.PhotoImage(resized_img)
      leo_text = ImageTk.PhotoImage(resized_img_text)
      leo_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 14:
      print(n)
      lucas = ImageTk.PhotoImage(resized_img)
      lucas_text = ImageTk.PhotoImage(resized_img_text)
      lucas_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 15:
      print(n)
      mason = ImageTk.PhotoImage(resized_img)
      mason_text = ImageTk.PhotoImage(resized_img_text)
      mason_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 16:
      print(n)
      max = ImageTk.PhotoImage(resized_img)
      max_text = ImageTk.PhotoImage(resized_img_text)
      max_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 17:
      print(n)
      muhammad = ImageTk.PhotoImage(resized_img)
      muhammad_text = ImageTk.PhotoImage(resized_img_text)
      muhammad_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 18:
      print(n)
      rosie = ImageTk.PhotoImage(resized_img)
      rosie_text = ImageTk.PhotoImage(resized_img_text)
      rosie_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 19:
      print(n)
      ruby = ImageTk.PhotoImage(resized_img)
      ruby_text = ImageTk.PhotoImage(resized_img_text)
      ruby_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 20:
      print(n)
      sebastian = ImageTk.PhotoImage(resized_img)
      sebastian_text = ImageTk.PhotoImage(resized_img_text)
      sebastian_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 21:
      print(n)
      shabina = ImageTk.PhotoImage(resized_img)
      shabina_text = ImageTk.PhotoImage(resized_img_text)
      shabina_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 22:
      print(n)
      steve = ImageTk.PhotoImage(resized_img)
      steve_text = ImageTk.PhotoImage(resized_img_text)
      steve_zoom = ImageTk.PhotoImage(resized_img_zoom)
    elif i == 23:
      print(n)
      tamako = ImageTk.PhotoImage(resized_img)
      tamako_text = ImageTk.PhotoImage(resized_img_text)
      tamako_zoom = ImageTk.PhotoImage(resized_img_zoom)
  #Update#
  print('96%')
  #_____Select_person_image_function_____#
  def select_image():
    global image_baisse
    global nb_click_btn_try
    if nb_click_btn_try == 0:
      image_baisse = 2
      btn_try.config(text="Annuler l'opération")
      nb_click_btn_try = 1
    elif nb_click_btn_try == 1:
      image_baisse = 0
      btn_try.config(text="Cliquer ici pour\nselectionner le\npersonnage")
      nb_click_btn_try = 0
  #_____Click_on_image_____#
  def click_image(image, btn_image, image1, name):
    global image_baisse
    global score
    if image_baisse == 0:
      btn_image.config(image=image1)
      image_baisse = 1
    elif image_baisse == 1:
      btn_image.config(image=image)
      image_baisse = 0
    elif image_baisse == 2:
      verify_answer(name, functions.randomperso.selected_person)
      #_____Status_window_____#
      if functions.randomperso.status == 'winner':
        #_____Window_parameters_____#
        win_root = Toplevel()
        win_root.geometry('350x200+200+175')
        win_root.overrideredirect(True)
        win_root.resizable(False, False)
        win_root.configure(background=background_color) #white
        font_color = "#124179"  #blue
        #_____Destroy_function_____#
        def destroy_all():
          window_destroy(play_root)
          window_destroy(win_root)
        #_____Widgets_defining_____#
        #lb_win#
        lb_win = Label(win_root, text=f'Felicitations! Vous avez devinez\nle personnage: {functions.randomperso.selected_person}.', fg=font_color, bg='white', font=('arial',13))
        lb_win.place(x=175, y=40, anchor=CENTER)
        #btn_win#
        btn_win = Button(win_root, text="Retour au\nmenu.", fg=font_color, bg='white', activeforeground=font_color, font=('arial', 13), command=destroy_all, relief=FLAT)
        btn_win.place(x=2, y=198, anchor=SW)
        #btn_win_quit#
        btn_win_quit = Button(win_root, text="     Fermer      \n", fg=font_color, bg='white', activeforeground=font_color, font=('arial', 13), command=lambda *args: window_destroy(win_root), relief=FLAT)
        btn_win_quit.place(x=348, y=198, anchor=SE)
        #lb_win_score#
        lb_win_score = Label(win_root, text=f'Votre score: {score}', fg=font_color, bg='white', font=('arial',13, 'underline'))
        lb_win_score.place(x=175, y=90, anchor=CENTER)
      elif functions.randomperso.status == 'loser':
        score += 1
        lb_score.config(text=f'Score: {score}')
        #_____Window_parameters_____#
        lose_root = Toplevel()
        lose_root.geometry('350x200+200+150')
        lose_root.overrideredirect(True)
        lose_root.resizable(False, False)
        lose_root.configure(background=background_color)
        font_color = "#124179"  #blue
        #_____Destroy_function_____#
        def destroy_everything():
          play_root.destroy()
          lose_root.destroy()
        #_____Answer_reveal_function_____#
        def show_person():
          btn_lose.destroy()
          btn_lose_quit.destroy()
          #_____Widgets_defining_____#
          #lb_answer_shown#
          lb_answer_shown = Label(lose_root, text=f'La réponse était:\n{functions.randomperso.selected_person}.', fg=font_color, bg='white', font=('arial',13, 'italic'))
          lb_answer_shown.place(x=175, y=130, anchor=CENTER)
          #btn_definitive_quit#
          btn_definitive_quit = Button(lose_root, text='QUITTER', command=destroy_everything, fg=font_color, bg='white', activeforeground=font_color, font=('arial', 13), relief=FLAT)
          btn_definitive_quit.place(x=175, y=198, anchor=S)
        #_____Widgets_defining_____#
        #lb_lose#
        lb_lose = Label(lose_root, text=f"Dommage ce n'est\npas le bon personnage.\nRetentez votre chance.", fg=font_color, bg='white', font=('arial',13))
        lb_lose.place(x=175, y=40, anchor=CENTER)
        #btn_lose_quit#
        btn_lose_quit = Button(lose_root, text="     Fermer     ", fg=font_color, bg='white', activeforeground=font_color, font=('arial', 13), command=lambda *args: window_destroy(lose_root), relief=FLAT)
        btn_lose_quit.place(x=348, y=198, anchor=SE)
        #btn_lose#
        btn_lose = Button(lose_root, text='     Quitter     ', fg=font_color, bg='white', activeforeground=font_color, font=('arial', 13), command=show_person, relief=FLAT)
        btn_lose.place(x=2, y=198, anchor=SW)
        #lb_lose_score
        lb_lose_score = Label(lose_root, text=f'Votre score: {score}', fg=font_color, bg='white', font=('arial',13, 'underline'))
        lb_lose_score.place(x=175, y=90, anchor=CENTER)
  #_____Images_positioning_table_____#
  tableau_coordonnees = [[0, 0], [80, 0], [160, 0], [240, 0], [320, 0],[400, 0], [0, 110], [80, 110], [160, 110], [240, 110], [320, 110], [400, 110], [0, 220],[80, 220], [160, 220], [240, 220], [320, 220],[400, 220], [0, 330], [80, 330], [160, 330],[240, 330], [320, 330], [400, 330]]
  #_____Images_positioning_program_____#
  x_y = []
  for i in range(24):
    nb_gen = randint(0, len(tableau_coordonnees) - 1)
    x_y.append(tableau_coordonnees[nb_gen][0])
    x_y.append(tableau_coordonnees[nb_gen][1])
    del tableau_coordonnees[nb_gen]
  #_____Selection_of_categorie_____#
  def selected_1(select):
    #_____Global_values_____#
    global under_categories
    global optionmenu_update
    global option_menu_2
    global select_1
    global score
    global history
    #_____Values_____#
    variable_1 = StringVar()
    select_1 = variable.get()
    #_____Selected_categorie_interpretation_____#
    if select == 'Sexe':
      under_categories = ['Homme', 'Femme']
      variable_1.set('Homme')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Cheveux':
      under_categories = ['Blond', 'Brun', 'Roux', 'Noir', 'Gris', 'Bouclés', 'Lisse']
      variable_1.set('Blond')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Poils':
      under_categories = ['Moustache', 'Barbe']
      variable_1.set('Moustache')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Accessoire(s)':
      under_categories = ['Collier', "Boucles d'oreilles", 'Lunettes', 'Fleur', 'Bandanna', 'Casque', 'Noeud de papillon']
      variable_1.set('Collier')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Couvre-chef':
      under_categories = ['Casquette', 'Bonnet']
      variable_1.set('Casquette')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Yeux':
      under_categories = ['Marron', 'Vert', 'Bleu', 'Noir', 'Inconnu']
      variable_1.set('Marron')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    elif select == 'Peau':
      under_categories = ['Clair', 'Foncé']
      variable_1.set('Clair')
      select_label_2.config(text=f'Parmi la catégorie "{select}" séléctionner une sous-catégorie: ')
    #_____Selection_sub-categorie_____#
    def selected_2():
      global select
      global score
      global history
      #_____Values_____#
      score += 1
      select_2 = variable_1.get()
      reponse(select_1, select_2)
      new_question = f' - {select_1} - {select_2}:\n       - {functions.randomperso.answer}\n'
      history = history + new_question
      #_____Widgets_configuration_____#
      lb_score.config(text=f'Score: {score}')
      lb_answer.config(text=f'La réponse\nest:\n -  {functions.randomperso.answer}')
      lb_note.config(highlightthickness=2)
      lb_note.config(text=history)
      return select_1
    #_____Change_categorie_selected_____#
    if optionmenu_update == True:
      option_menu_2.destroy()
    #_____Second_option_menu_____#
    option_menu_2 = OptionMenu(play_root, variable_1, *under_categories)
    option_menu_2.config(bg="white", fg=font_color, activeforeground=font_color, relief=FLAT)
    option_menu_2.config(font=('arial', 13))
    option_menu_2['menu'].config(bg='white')
    option_menu_2['highlightthickness'] = 1
    option_menu_2.place(x=135, y=550)
    #_____Values_____#
    optionmenu_update = True
    #_____Widgets_defining_____#
    #btn_confirm#
    btn_confirm = Button(play_root, text='  Valider  ', command=selected_2, foreground=font_color, background='white', font=('arial', 13), relief=FLAT, activeforeground=font_color)
    btn_confirm.place(x=340, y=550)
    #_____Return_____#
    return under_categories
  #_____Widgets_defining_____#
  #select_label_1#
  select_label_1 = Label(play_root, text='Veuillez slectionner une des catégories proposées: ', foreground=font_color, background='white', font=('arial', 13))
  select_label_1.place(x=5, y=460)
  #_____Words_propositions_____#
  categories = ['Sexe', 'Cheveux', 'Poils', 'Accessoire(s)', 'Couvre-chef', 'Yeux', 'Peau']
  #_____Values_____#
  variable = StringVar()
  variable.set('Sexe')
  #_____First_option_menu_____#
  option_menu_1 = OptionMenu(play_root, variable, *categories, command=selected_1)
  option_menu_1.config(bg="white", fg=font_color, activeforeground=font_color, relief=FLAT)
  option_menu_1.config(font=('arial', 13))
  option_menu_1['menu'].config(bg='white')
  option_menu_1['highlightthickness'] = 1
  option_menu_1.place(x=135, y=485)
  #_____Widgets_defining_____#
  #select_label_2#
  select_label_2 = Label(play_root, text=" ", foreground=font_color, background='white', font=('arial', 13))
  select_label_2.place(x=5, y=523)
  #lb_zoom#
  lb_zoom = Label(play_root, image=andre_zoom, bg='white')
  lb_zoom.place(x=480, y=0)
  #_____Zoom_function_____#
  def zoom(name_zoom):
    lb_zoom.config(image=name_zoom)
  #_____Bind_function_____#
  def bind(name, btn_name, name_text, name_zoom, name_person):
    btn_name.bind('<Button-1>', lambda *args: click_image(name, btn_name, name_text, name_person))
    btn_name.bind('<Button-3>', lambda *args: zoom(name_zoom))
#Update#
  print('98%')
  #_____Widgets_defining_____#
  #Andre
  btn_andre = Button(play_root, image=andre, bg='white', activebackground='white', highlightthickness=0)
  btn_andre.place(x=x_y[0], y=x_y[1])
  bind(andre, btn_andre, andre_text, andre_zoom, "Andre")
  #Ayan
  btn_ayan = Button(play_root, image=ayan, bg='white', activebackground='white', highlightthickness=0)
  btn_ayan.place(x=x_y[2], y=x_y[3])
  bind(ayan, btn_ayan, ayan_text, ayan_zoom, 'Ayan')
  #Chris
  btn_chris = Button(play_root, image=chris, bg='white', activebackground='white')
  btn_chris.place(x=x_y[4], y=x_y[5])
  bind(chris, btn_chris, chris_text, chris_zoom, 'Chris')
  #Daniel
  btn_daniel = Button(play_root, image=daniel, bg='white', activebackground='white')
  btn_daniel.place(x=x_y[6], y=x_y[7])
  bind(daniel, btn_daniel, daniel_text, daniel_zoom, 'Daniel')
  #Eva
  btn_eva = Button(play_root, image=eva, bg='white', activebackground='white')
  btn_eva.place(x=x_y[8], y=x_y[9])
  bind(eva, btn_eva, eva_text, eva_zoom, 'Eva')
  #Fred
  btn_fred = Button(play_root, image=fred, bg='white', activebackground='white')
  btn_fred.place(x=x_y[10], y=x_y[11])
  bind(fred, btn_fred, fred_text, fred_zoom, 'Fred')
  #George
  btn_george = Button(play_root, image=george, bg='white', activebackground='white')
  btn_george.place(x=x_y[12], y=x_y[13])
  bind(george, btn_george, george_text, george_zoom, 'George')
  #Georgia
  btn_georgia = Button(play_root, image=georgia, bg='white', activebackground='white')
  btn_georgia.place(x=x_y[14], y=x_y[15])
  bind(georgia, btn_georgia, georgia_text, georgia_zoom, 'Georgia')
  #Greg
  btn_greg = Button(play_root, image=greg, bg='white', activebackground='white')
  btn_greg.place(x=x_y[16], y=x_y[17])
  bind(greg, btn_greg, greg_text, greg_zoom, 'Greg')
  #Harriet
  btn_harriet = Button(play_root, image=harriet, bg='white', activebackground='white')
  btn_harriet.place(x=x_y[18], y=x_y[19])
  bind(harriet, btn_harriet, harriet_text, harriet_zoom, 'Harriet')
  #Isobel
  btn_isobel = Button( play_root, image=isobel, bg='white', activebackground='white')
  btn_isobel.place(x=x_y[20], y=x_y[21])
  bind(isobel, btn_isobel, isobel_text, isobel_zoom, 'Isobel')
  #Jayden
  btn_jayden = Button(play_root, image=jayden, bg='white', activebackground='white')
  btn_jayden.place(x=x_y[22], y=x_y[23])
  bind(jayden, btn_jayden, jayden_text, jayden_zoom, 'Jayden')
  #Jess
  btn_jess = Button(play_root, image=jess, bg='white', activebackground='white')
  btn_jess.place(x=x_y[24], y=x_y[25])
  bind(jess, btn_jess, jess_text, jess_zoom, 'Jess')
  #Leo
  btn_leo = Button(play_root, image=leo, bg='white', activebackground='white')
  btn_leo.place(x=x_y[26], y=x_y[27])
  bind(leo, btn_leo, leo_text, leo_zoom, 'Leo')
  #Lucas
  btn_lucas = Button( play_root, image=lucas, bg='white', activebackground='white')
  btn_lucas.place(x=x_y[28], y=x_y[29])
  bind(lucas, btn_lucas, lucas_text, lucas_zoom, 'Lucas')
  #Lucas
  btn_mason = Button(play_root, image=mason, bg='white', activebackground='white')
  btn_mason.place(x=x_y[30], y=x_y[31])
  bind(mason, btn_mason, mason_text, mason_zoom, 'Mason')
  #Max
  btn_max = Button(play_root, image=max, bg='white', activebackground='white')
  btn_max.place(x=x_y[32], y=x_y[33])
  bind(max, btn_max, max_text, max_zoom, 'Max')
  #Muhammad
  btn_muhammad = Button(play_root, image=muhammad, bg='white', activebackground='white')
  btn_muhammad.place(x=x_y[34], y=x_y[35])
  bind(muhammad, btn_muhammad, muhammad_text, muhammad_zoom, 'Muhammad')
  #Rosie
  btn_rosie = Button(play_root, image=rosie, bg='white', activebackground='white')
  btn_rosie.place(x=x_y[36], y=x_y[37])
  bind(rosie, btn_rosie, rosie_text, rosie_zoom, 'Rosie')
  #Ruby
  btn_ruby = Button(play_root, image=ruby, bg='white',activebackground='white')
  btn_ruby.place(x=x_y[38], y=x_y[39])
  bind(ruby, btn_ruby, ruby_text, ruby_zoom, 'Ruby')
  #Sebastian
  btn_sebastian = Button(play_root, image=sebastian, bg='white', activebackground='white')
  btn_sebastian.place(x=x_y[40], y=x_y[41])
  bind(sebastian, btn_sebastian, sebastian_text, sebastian_zoom, 'Sebastian')
  #Shabina
  btn_shabina = Button(play_root,image=shabina, bg='white',activebackground='white')
  btn_shabina.place(x=x_y[42], y=x_y[43])
  bind(shabina, btn_shabina, shabina_text, shabina_zoom, 'Shabina')
  #Steve
  btn_steve = Button(play_root, image=steve, bg='white',activebackground='white')
  btn_steve.place(x=x_y[44], y=x_y[45])
  bind(steve, btn_steve, steve_text, steve_zoom, 'Steve')
  #Tamako
  btn_tamako = Button(play_root,image=tamako, bg='white', activebackground='white')
  btn_tamako.place(x=x_y[46], y=x_y[47])
  bind(tamako, btn_tamako, tamako_text, tamako_zoom, 'Tamako')

  #btn_quit#
  btn_quit = Button(play_root, text='QUITTER', bg="white", foreground=font_color, activeforeground=font_color, command=lambda *args: window_destroy(play_root), relief=FLAT)
  btn_quit.place(x=748, y=4, anchor=NE)
  #lb_answer#
  lb_answer = Label(play_root, text="La réponse\ns'affichera\nici.", foreground=font_color, bg='white', justify=LEFT, font=('arial', 13))
  lb_answer.place(x=622, y=50)
  #lb_score#
  lb_score = Label(play_root, text='Score: ', bg='white', fg=font_color, justify=CENTER, font=('arial', 13))
  lb_score.place(x=625, y=150)
  #lb_score#
  lb_note = Label(play_root, text='', bg='white', font=('arial', 13), fg=font_color, justify=LEFT, highlightthickness=0)
  lb_note.place(x=480, y=210)
  #btn_try#
  btn_try = Button(play_root, text='Cliquer ici\npour\nselectionner\nle personnage.', fg=font_color, bg='white', justify=LEFT, relief=FLAT, command=select_image, activeforeground=font_color)
  btn_try.place(x=748, y=596, anchor=SE)
  #Update
  print('100%')