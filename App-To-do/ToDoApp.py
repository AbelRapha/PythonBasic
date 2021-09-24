import builtins
from tkinter import *
from tkinter.font import BOLD
from tkinter import Listbox
from baseDeDados import *

colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00", "Green":"#42f560", "Red":"#ba290f"}

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


def main(a):
    ### Novo 
    if a == "Novo":

        for widget in frame_esquerdo_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            entrada_tarefa = inserindo_tarefa.get()
            inserir([entrada_tarefa])
            mostrar()

        label_inserir_tarefa = Label(frame_esquerdo_baixo, text="Insira nova Tarefa", font=(BOLD, 12),
 fg=colors["black"], width=30, height=5, pady= 12,
padx= 10, relief='flat', anchor=CENTER ,bg=colors["white"])

        label_inserir_tarefa.grid(row=0,column=0)

        inserindo_tarefa = Entry(frame_esquerdo_baixo, width=15, font=(BOLD,12))

        inserindo_tarefa.grid(row=1,column=0,sticky=NSEW)

        #Criando botao de adicionar:
        botao_adiciona = Button(frame_esquerdo_baixo, text="Adicionar", bg=colors["Green"],
 fg=colors["black"], font= (BOLD,15), anchor=CENTER, 
 relief=RAISED, width=10, height=1, command= adicionar)
        botao_adiciona.grid(row=2,column=0, pady=40)
    ### Renomear
    if a == "Renomear":
        for widget in frame_esquerdo_baixo.winfo_children():
            widget.destroy()
        
        #Quando o usuario selecionar o item da listbox a ser renomeado
        def on():
            
            label_renomear_tarefa = Label(frame_esquerdo_baixo, text="Renomeie a Tarefa", font=(BOLD, 12),
        fg=colors["black"], width=30, height=5, pady= 12,
        padx= 10, relief='flat', anchor=CENTER ,bg=colors["white"])
            label_renomear_tarefa.grid(row=0,column=0)
            renomeando_tarefa = Entry(frame_esquerdo_baixo, width=15, font=(BOLD,12))
            renomeando_tarefa.grid(row=1,column=0,sticky=NSEW)
            
            valor_selecionado = listbox.curselection()[0]
            palavra_selecionada = listbox.get(valor_selecionado)
            renomeando_tarefa.insert(0,palavra_selecionada)
            #Chamando o banco de dados
            tarefas = selecionar()
    
            #Criando botao de renomear:

            def renomearToDo():
                for item in tarefas:
                    if palavra_selecionada == item[1]:
                        nova_palavra = [renomeando_tarefa.get(), item[0]]
                        renomear(nova_palavra)
                        renomeando_tarefa.delete(0,END)
                mostrar()

            botao_renomeia = Button(frame_esquerdo_baixo, text="Alterar", bg=colors["Red"],
            fg=colors["white"], font= (BOLD,15), anchor=CENTER, 
            relief=RAISED, width=10, height=1, command= renomearToDo)
            botao_renomeia.grid(row=2,column=0, pady=40)

        on()


##Criando a função para remover elementos do To Do list

def removerTodo():
    valor_selecionado = listbox.curselection()[0]
    palavra_selecionada = listbox.get(valor_selecionado)
    #Chamando o banco de dados
    tarefas = selecionar()
    
    #Criando botao de remover:
    for item in tarefas:
        if palavra_selecionada == item[1]:
            deletar([item[0]])
    mostrar()    

#Criando os botoes Novo,Remover e Renomear

botao_novo = Button(frame_esquerdo_cima, text="Novo", bg=colors["Blue"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1, command= lambda: main("Novo"))
botao_novo.grid(row=0,column=0, sticky=NSEW, pady=1)

botao_remover = Button(frame_esquerdo_cima, text="Remover", bg=colors["Orange"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1, command= removerTodo)
botao_remover.grid(row=0,column=1, sticky=NSEW, pady=1)

botao_renomear = Button(frame_esquerdo_cima, text="Renomear", bg=colors["Gray"],
 fg=colors["white"], font= (BOLD,12), anchor=CENTER, 
 relief=RAISED, width=10, height=1, command=lambda: main("Renomear"))
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


def mostrar():
    listbox.delete(0,END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END,item[1])

try:
    mostrar()
except (lite.OperationalError):
    criarTabela()
else:
    mostrar()

janela.mainloop()

