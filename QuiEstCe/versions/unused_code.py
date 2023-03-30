  '''
x_y = [[andre_x, andre_y], [ayan_x, ayan_y], [chris_x, chris_y], [daniel_x, daniel_y], [eva_x, eva_y], [fred_x, fred_y], [george_x, george_y], [georgia_x, georgia_y], [greg_x, greg_y], [harriet_x, harriet_y], [isobel_x, isobel_y], [jayden_x, jayden_y], [jess_x, jess_y], [leo_x, leo_y], [lucas_x, lucas_y], [mason_x, mason_y], [max_x, max_y], [muhammad_x, muhammad_y], [rosie_x, rosie_y], [ruby_x, ruby_y], [sebastian_x, sebastian_y], [shabina_x, shabina_y], [steve_x, steve_y], [tamako_x, tamako_y]]
'''

    '''
    global img_andre
    global img_ayan
    global img_chris
    global img_daniel
    global img_eva
    global img_fred
    global img_george 
    global img_georgia 
    global img_greg 
    global img_harriet 
    global img_isobel
    global img_jayden 
    global img_jess 
    global img_leo 
    global img_lucas 
    global img_mason 
    global img_max 
    global img_muhammad 
    global img_rosie 
    global img_ruby 
    global img_sebastian 
    global img_shabina 
    global img_steve 
    global img_tamako
    '''

'''
  img_andre = 0
  img_ayan = 0
  img_chris = 0
  img_daniel = 0
  img_eva = 0
  img_fred = 0
  img_george = 0
  img_georgia = 0
  img_greg = 0
  img_harriet = 0
  img_isobel = 0
  img_jayden = 0
  img_jess = 0
  img_leo = 0
  img_lucas = 0
  img_mason = 0
  img_max = 0
  img_muhammad = 0
  img_rosie = 0
  img_ruby = 0
  img_sebastian = 0
  img_shabina = 0
  img_steve = 0
  img_tamako = 0
  '''

'''
from tkinter import *

from functions.jouer import *

def load():
  global load_lb
  load_root = Toplevel()
  load_root.geometry("900x500")
  load_root.title("        Qui Est-Ce ?")
  load_root.overrideredirect(True)
  load_root.resizable(False, False)
  load_root.config(bg='blue')

  load_lb = Label(load_root, text='loading page')
  load_lb.place(x=0, y=0)

  jouer()

  #load.mainloop()
'''

#lambda event=None:btn_andre.invoke())

#  btn_ayan = Button(play_root, image=ayan, command=lambda *args: click_image(ayan, btn_ayan, ayan_text), bg='white', activebackground='white')


'''
  btn_andre.bind('<Button-1>', lambda *args: click_image(andre, btn_andre, andre_text))
  btn_andre.bind('<Button-3>', lambda *args: zoom(andre_zoom)
  btn_ayan.bind('<Button-1>', lambda *args: click_image(ayan, btn_ayan, ayan_text))
  btn_ayan.bind('<Button-3>', lambda *args: zoom(ayan_zoom)
  btn_chris.bind('<Button-1>', lambda *args: click_image(chris, btn_chris, chris_text))
  btn_chris.bind('<Button-3>', lambda *args: zoom(chris_zoom)
  btn_daniel.bind('<Button-1>', lambda *args: click_image(daniel, btn_daniel, daniel_text))
  btn_daniel.bind('<Button-3>', lambda *args: zoom(daniel_zoom)
  btn_eva.bind('<Button-1>', lambda *args: click_image(eva, btn_eva, eva_text))
  btn_eva.bind('<Button-3>', lambda *args: zoom(eva_zoom)
  btn_fred.bind('<Button-1>', lambda *args: click_image(fred, btn_fred, fred_text))
  btn_fred.bind('<Button-3>', lambda *args: zoom(fred_zoom)
  btn_george.bind('<Button-1>', lambda *args: click_image(george, btn_george, george_text))
  btn_george.bind('<Button-3>', lambda *args: zoom(george_zoom)
    btn_georgia.bind('<Button-1>', lambda *args: click_image(georgia, btn_georgia, georgia_text))
  btn_georgia.bind('<Button-3>', lambda *args: zoom(georgia_zoom)
  btn_greg.bind('<Button-1>', lambda *args: click_image(greg, btn_greg, greg_text))
  btn_greg.bind('<Button-3>', lambda *args: zoom(greg_zoom)
  btn_harriet.bind('<Button-1>', lambda *args: click_image(harriet, btn_harriet, harriet_text))
  btn_harriet.bind('<Button-3>', lambda *args: zoom(harriet_zoom)
  btn_isobel.bind('<Button-1>', lambda *args: click_image(isobel, btn_isobel, isobel_text))
  btn_isobel.bind('<Button-3>', lambda *args: zoom(isobel_zoom)
  btn_jayden.bind('<Button-1>', lambda *args: click_image(jayden, btn_jayden, jayden_text))
  btn_jayden.bind('<Button-3>', lambda *args: zoom(jayden_zoom)
  btn_jess.bind('<Button-1>', lambda *args: click_image(jess, btn_andre, jess_text))
  btn_jess.bind('<Button-3>', lambda *args: zoom(jess_zoom)
  btn_leo.bind('<Button-1>', lambda *args: click_image(leo, btn_leo, leo_text))
  btn_leo.bind('<Button-3>', lambda *args: zoom(leo_zoom)
  btn_lucas.bind('<Button-1>', lambda *args: click_image(lucas, btn_lucas, lucas_text))
  btn_lucas.bind('<Button-3>', lambda *args: zoom(lucas_zoom)
  btn_mason.bind('<Button-1>', lambda *args: click_image(mason, btn_mason, mason_text))
  btn_mason.bind('<Button-3>', lambda *args: zoom(mason_zoom)
  btn_max.bind('<Button-1>', lambda *args: click_image(max, btn_max, max_text))
  btn_max.bind('<Button-3>', lambda *args: zoom(max_zoom)
  btn_muhammad.bind('<Button-1>', lambda *args: click_image(muhammad, btn_muhammad, muhammad_text))
  btn_muhammad.bind('<Button-3>', lambda *args: zoom(muhammad_zoom)
  btn_rosie.bind('<Button-1>', lambda *args: click_image(rosie, btn_rosie, rosie_text))
  btn_rosie.bind('<Button-3>', lambda *args: zoom(rosie_zoom)
  btn_ruby.bind('<Button-1>', lambda *args: click_image(ruby, btn_ruby, ruby_text))
  btn_ruby.bind('<Button-3>', lambda *args: zoom(ruby_zoom)
  btn_sebastian.bind('<Button-1>', lambda *args: click_image(sebastian, btn_sebastian, sebastian_text))
  btn_sebastian.bind('<Button-3>', lambda *args: zoom(sebastian_zoom)
  btn_shabina.bind('<Button-1>', lambda *args: click_image(shabina, btn_shabina, shabina_text))
  btn_shabina.bind('<Button-3>', lambda *args: zoom(shabina_zoom)
  btn_steve.bind('<Button-1>', lambda *args: click_image(steve, btn_steve, steve_text))
  btn_steve.bind('<Button-3>', lambda *args: zoom(steve_zoom)
  btn_tamako.bind('<Button-1>', lambda *args: click_image(tamako, btn_tamako, tamako_text))
  btn_tamako.bind('<Button-3>', lambda *args: zoom(tamako_zoom)
'''