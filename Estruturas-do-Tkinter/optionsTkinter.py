import tkinter as tk
from tkinter import ttk

window = tk.Tk()

#Ajustando as janelas para não deformarem
window.rowconfigure(0, weight=1) #weight=0 sem redirecionamento automático 1 de forma automática
window.columnconfigure([0,1],weight=1)

var_promotions = tk.IntVar()
checkbox_promotions = tk.Checkbutton(text="Deseja receber e-mails promocionais? ", variable=var_promotions)
checkbox_promotions.grid(row=0, column=0)

var_politics = tk.IntVar()
checkbox_politics = tk.Checkbutton(text="Deseja receber e-mails promocionais? ", variable=var_politics)
checkbox_politics.grid(row=1, column=0)

def enviar():
    if var_promotions.get():
        print("O usuário deseja receber promoções")
    else:
        print("Usuário não deseja receber promoções")
    if var_politics.get():
        print("O usuário Concordou com as políticas de uso e privacidade")
    else:
        print("O usuário Não Concordou com as políticas de uso e privacidade")

button_send = tk.Button(text="Enviar", command=enviar)
button_send.grid(row=2, column=0)

#Radio Buttons

var_airplane = tk.StringVar(value="Null")

def send_class():
    print(var_airplane.get())

button_economic_class = tk.Radiobutton(text='Classe Econômica', variable=var_airplane, value="Classe Econômica", command=send_class)
button_executive_class = tk.Radiobutton(text='Classe Executiva', variable=var_airplane, value="Classe Executiva", command=send_class)
button_top_class = tk.Radiobutton(text='Primeira Classe', variable=var_airplane, value="Primeira Classe", command=send_class)

#Grid
button_economic_class.grid(row=3, column=0)
button_executive_class.grid(row=3, column=1)
button_top_class.grid(row=3, column=2)

button_send_class = tk.Button(text='Enviar', command=send_class)
button_send_class.grid(row=4,column=0 )

window.mainloop()