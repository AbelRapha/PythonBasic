from tkinter import *
from tkinter import font
from PIL import Image
from tkinter import filedialog as fd
from tkinter import messagebox


colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00"}

def NovoArquivo():
    #Selecionar o arquivo
    nome_do_arquivo = fd.askopenfilename()
    img = Image.open(nome_do_arquivo)

    #Tamanho da imagem original

    img_altura, img_largura=img.size

    #Funcao para converter o tamanho da imagem

    def converter():
        #Obtendo os valores da Altura e Largura A partir do Entry
        altura = int(entrada_altura.get())
        largura = int(entrada_largura.get())

        #Uso da Biblioteca Pillow
        novo_valor = (altura,largura)
        nova_imagem = img.resize(novo_valor)     
        #Salvando a Nova imagem
        img_a_salvar = fd.asksaveasfile()
        nova_imagem.save(img_a_salvar.name + ".JPG")   

        #Mensagem de conclusao da conversao
        messagebox.showinfo("Sucesso", "A imagem foi convertida com Sucesso!!!")

        tamanho_original.destroy()
        nova_altura.destroy()
        nova_largura.destroy()
        entrada_largura.destroy()
        entrada_altura.destroy()
        botao.destroy()


    tamanho_original = Label(frame,text="Altura e Largura Original " + str(img_altura)+"x"+str(img_largura),
 font=("Courier 13 bold"), width= 25, 
 height=1,anchor=CENTER, pady=7, padx=10, relief="flat", 
 bg = colors["white"], fg=colors["Blue"])
    tamanho_original.grid(row=2, column=0, columnspan=2,sticky=NSEW, pady=1)
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
    bg = colors["Orange"], fg=colors["black"], command=converter)

    botao.grid(row=6, column=0, columnspan=2,pady=2)


janela = Tk()
janela.title("Redimensionador de imagem")
janela.geometry("450x290")
janela.configure(bg=colors["white"])

#Criação do Frame
frame = Frame(janela,width= 450, height= 275, bg=colors["white"], relief="flat")
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
 bg = colors["Blue"], fg=colors["black"],command= NovoArquivo)

botao.grid(row=1, column=0, columnspan=2,sticky=NSEW, pady=1)



janela.mainloop()