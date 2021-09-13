from tkinter import * 
from tkinter import ttk

colors = {"black": "#050505", "white": "#ffffff", "Blue": "#39579e" , "Gray": "#48494a", "Orange":"#e89b00"}

janela = Tk()
janela.title("Calculator")
janela.geometry("250x323")
janela.config(bg = colors["Gray"])

#Criação dos Frames
frame_tela = Frame(janela, width=250, height= 60, background=colors["Gray"])
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela,width= 250, height=263)
frame_corpo.grid(row=1,column=0)

#Variável Todos os valores
todos_valores = ''
#Criando as expressões matemáticas

def entrar_valores(evento):
    global todos_valores

    todos_valores =  todos_valores + str(evento)
    #Passando valor para tela
    valor_texto.set(todos_valores)

#Função para calcular 
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

#Função que limpa a Tela
def LimpaTela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=17,height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT,font= ('Ivy 18 '), bg=colors["Gray"], fg=colors["white"])
app_label.place(x =0, y=0)


#Criando os botões
button_clear = Button(frame_corpo,command= LimpaTela,text="C", width= 9, height=2, bg= colors["white"], fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_clear.place(x=0, y=0)

button_percent = Button(frame_corpo,command= lambda: entrar_valores('%'),text="%", width= 7, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_percent.place(x=100, y=0)

button_divisor = Button(frame_corpo,command= lambda: entrar_valores('/'),text="/", width= 7, height=2, bg= colors["Orange"],fg=colors["white"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_divisor.place(x=180, y=0)

button_seven = Button(frame_corpo,command= lambda: entrar_valores('7'),text="7", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_seven.place(x=0, y=53)

button_eight = Button(frame_corpo,command= lambda: entrar_valores('8'),text="8", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_eight.place(x=60, y=53)

button_nine = Button(frame_corpo,command= lambda: entrar_valores('9'),text="9", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_nine.place(x=120, y=53)

button_multiplier = Button(frame_corpo,command= lambda: entrar_valores('*'),text="X", width= 6, height=2, bg= colors["Orange"],fg=colors["white"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_multiplier.place(x=180, y=53)

button_four = Button(frame_corpo,command= lambda: entrar_valores('4'),text="4", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_four.place(x=0, y=106)

button_five = Button(frame_corpo,command= lambda: entrar_valores('5'),text="5", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_five.place(x=60, y=106)

button_six = Button(frame_corpo,command= lambda: entrar_valores('6'),text="6", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_six.place(x=120, y=106)

button_minus = Button(frame_corpo,command= lambda: entrar_valores('-'),text="-", width= 6, height=2, bg= colors["Orange"],fg=colors["white"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_minus.place(x=180, y=106)

button_one = Button(frame_corpo,command= lambda: entrar_valores('1'),text="1", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_one.place(x=0, y=159)

button_two = Button(frame_corpo,command= lambda: entrar_valores('2'),text="2", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_two.place(x=60, y=159)

button_three = Button(frame_corpo,command= lambda: entrar_valores('3'),text="3", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_three.place(x=120, y=159)

button_plus = Button(frame_corpo,command= lambda: entrar_valores('+'),text="+", width= 6, height=2, bg= colors["Orange"],fg=colors["white"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_plus.place(x=180, y=159)

button_zero = Button(frame_corpo,command= lambda: entrar_valores('0'),text="0", width= 11, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_zero.place(x=0, y=212)

button_point = Button(frame_corpo,command= lambda: entrar_valores('.'),text=".", width= 5, height=2, bg= colors["white"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_point.place(x=120, y=212)

button_equal = Button(frame_corpo,command = calcular,text="=", width= 6, height=2, bg= colors["Gray"],fg=colors["black"], font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_equal.place(x=180, y=212)


janela.mainloop()