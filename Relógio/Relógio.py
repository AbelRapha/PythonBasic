from tkinter import *
import tkinter
from datetime import datetime

#Cores
colors = {"black":"#000000", "white":"#ffffff", "red":"#e30914","green":"#22e309", "gray":"#717370","blue":"#1326a8"}

fundo = colors["gray"]
cor = colors["white"]

janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width = False, height=False)
janela.configure(bg = colors["gray"])

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")

    dia_semana = tempo.strftime("%A")

    dia = tempo.day

    mes = tempo.strftime("%B")

    ano = tempo.strftime("%Y")

    label1.config(text=hora)
    label1.after(200,relogio)
    label2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/"+ str(ano))
#Criação das Labels:

label1 = Label(janela, text = "", font = ("Arial 80"), bg = fundo, fg= cor)
label1.grid(row=0, column=0, sticky=NW, padx=5)

label2 = Label(janela, text = "", font = ("Arial 20"), bg = fundo, fg= cor)
label2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()

janela.mainloop()

