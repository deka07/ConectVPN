import os
from tkinter import *
from tkinter import filedialog

def abrirArquivo():
    arquivo = filedialog.askopenfilename()
    return arquivo

def sair():
    exit() 

def conectar():
    return print('Deka e Kelly')

win = Tk()
win.title('ConectVPN Free')
win.geometry('370x140')

drt = Label(win, text='Diretório:')
drt.place(x=20, y=20)

ety_drt = Entry(win)
ety_drt.place(x=100, y=20)

btn = Button(win, text='DIR', command = abrirArquivo)
btn.place(x=300, y=17)

sta = Label(win, text='Situação:')
sta.place(x=20, y=60)

sta = Label(win, text=abrirArquivo())
sta.place(x=90, y=60)

btn2 = Button(win, text='Sair', command = sair)
btn2.place(x=170, y=100)

btn3 = Button(win, text='Conectar', command = conectar)
btn3.place(x=260, y=100)

win.mainloop()