import builtins
from tkinter import *
from tkinter.font import BOLD
from tkinter import Listbox
from baseDeDados import *

colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00"}

#Criando a Janela Principal
janela = Tk()
janela.resizable(width=False,height=False)
janela.geometry('500x255')
janela.title("To do App")
janela.configure(background=colors["Gray"])

#Dividindo a Janela em 2 partes com eixo vertical como referencia

frame_esquerdo = Frame(janela, width= 300, height= 200, bg=colors["white"], relief='flat')
frame_esquerdo.grid(row=0, column=0, sticky=NSEW)

frame_direito = Frame(janela, width= 300, height= 250, bg=colors["white"], relief='flat')
frame_direito.grid(row=0, column=1, sticky=NSEW)

#Dividindo o frame a ensquerda em duas partes

frame_esquerdo_cima = Frame(frame_esquerdo, width= 300, height= 50, bg=colors["white"], relief='flat')
frame_esquerdo_cima.grid(row=0, column=0, sticky=NSEW)

frame_esquerdo_baixo = Frame(frame_esquerdo, width= 300, height= 150, bg=colors["white"], relief='flat')
frame_esquerdo_baixo.grid(row=1, column=0, sticky=NSEW)

#Criando os botoes Novo,Remover e Renomear

botao_novo = Button(frame_esquerdo_cima, text="Novo", bg=colors["Blue"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1)
botao_novo.grid(row=0,column=0, sticky=NSEW, pady=1)

botao_remover = Button(frame_esquerdo_cima, text="Remover", bg=colors["Orange"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1)
botao_remover.grid(row=0,column=1, sticky=NSEW, pady=1)

botao_renomear = Button(frame_esquerdo_cima, text="Renomear", bg=colors["Gray"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1)
botao_renomear.grid(row=0,column=2, sticky=NSEW, pady=1)

#Criacao do Label no frame da Direita com o listbox

label_direito = Label(frame_direito, text="Tarefas", font=(BOLD, 20),
 fg=colors["black"], width=37, height=1, pady= 7,
padx= 10, relief='flat', anchor=W, justify=CENTER,
bg=colors["white"])
label_direito.grid(row=0,column=0)

#Asicionando o listbox

listbox = Listbox(frame_direito, font = (BOLD,12), width= 1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)

tarefas = selecionar()

for item in tarefas:
    listbox.insert(END,item)

print(tarefas)

janela.mainloop()

