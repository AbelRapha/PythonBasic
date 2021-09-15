from tkinter import *
from tkinter import font

colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00"}

janela = Tk()
janela.title("Redimensionador de imagem")
janela.geometry("400x250")
janela.configure(bg=colors["white"])

#Criação do Frame
frame = Frame(janela,width= 400, height= 250, bg=colors["white"], relief="flat")
frame.grid(row=0, column=0, sticky=NSEW)

#Label
nome_aplicacao = Label(frame,text="Compressor de Imagem",
 font=("Courier 20 bold"), width= 25, 
 height=1,anchor=CENTER, pady=7, padx=10, relief="flat", 
 bg = colors["white"], fg=colors["black"])
nome_aplicacao.grid(row=0, column=0, columnspan=2,sticky=NSEW, pady=1)

#Criacao do botao
botao = Button(frame,text="+ Novo",
 font=("Courier 20 bold"), width=10, 
 height=1,anchor=CENTER,relief=RAISED, 
 bg = colors["Blue"], fg=colors["black"])

botao.grid(row=1, column=0, columnspan=2,sticky=NSEW, pady=1)

nova_altura = Label(frame,text="Digite a nova altura",
 font=("Courier 10 bold"), width= 25, 
 height=1,anchor=CENTER, pady=7, padx=10, relief="flat", 
 bg = colors["white"], fg=colors["black"])
nova_altura.grid(row=3, column=0,sticky=NSEW, pady=5)

nova_largura = Label(frame,text="Digite a nova largura",
 font=("Courier 10 bold"), width= 25, 
 height=1,anchor=CENTER, pady=7, padx=10, relief="flat", 
 bg = colors["white"], fg=colors["black"])
nova_largura.grid(row=3, column=1,sticky=NSEW, pady=5)

entrada_altura = Entry(frame,width=5,justify=LEFT,
font=("Calibri 12") )
entrada_altura.grid(row=4, column=0,sticky=NSEW, pady=5, ipady=1)

entrada_largura = Entry(frame, width= 5, justify=RIGHT,
font=("Calibri 12"))
entrada_largura.grid(row=4, column=1,sticky=NSEW, pady=5, ipady=1)

#Criacao do botao Converter
botao = Button(frame,text="Converter",
 font=("Courier 20 bold"), width=10, 
 height=1,anchor=CENTER,relief=RAISED, 
 bg = colors["Orange"], fg=colors["black"])

botao.grid(row=6, column=0, columnspan=2,sticky=NSEW, pady=2)

janela.mainloop()