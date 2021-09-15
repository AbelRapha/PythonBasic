from tkinter import *
from tkinter import ttk

colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00"}

janela = Tk()

janela.geometry("800x380")
janela.title("Calculadora IRPF")
janela.config(bg= colors["Blue"])

# Criando o Cabecalho:
cabecalho = Frame(janela, width= 800, height=70, bg=colors["Orange"] )
cabecalho.grid(row=0,column=0)

label_cabecalho = Label(cabecalho,
                        text= "Calculadora IRPF",
                        font= ("Arial 18", 30),
                        justify=CENTER,
                        width= 20,
                        height=1,
                        bg= colors["Orange"],
                        fg= colors["white"],
                        padx= 7)
label_cabecalho.place(x=150,y=25)


#Criando o Corpo
corpo = Frame(janela, width= 200, height= 50)
corpo.grid(row=1,column=0)

label_corpo = Label(corpo,
                    text= "Teste",
                    font=("Arial 18", 30),
                    justify=LEFT,
                    width=20,
                    height=1,
                    fg=colors["black"])
label_corpo.place(x=-50,y=0 )

janela.mainloop()