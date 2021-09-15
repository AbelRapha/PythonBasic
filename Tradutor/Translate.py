from tkinter import * 
from tkinter import ttk, font, Button
from googletrans import Translator 

translator  = Translator()
def traduzir(evento=None):
    global entrada, combo_entrada,combo_saida
    texto = entrada.get('1.0','end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto,src=src,tgt=dest)
    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado)
    saida.configure(state='disabled')

janela = Tk()
janela.title("Tradutor")


values = ['pt', 'es', 'en']
#Entrada de Valores
frame_entrada = ttk.Frame()
label_entrada = ttk.Label(frame_entrada,text="Entrada", font=(None, 20))
combo_entrada = ttk.Combobox(frame_entrada,values= values, font=(None, 20))
combo_entrada.set("pt")


frame_entrada.grid(row = 0, column=0)
label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx = 30, pady=10)
frame_entrada.pack()
entrada = Text(height=10, width=50, font=(None,15))
entrada.pack(padx =10,pady=10, fill='both', expand='yes')

# Saida

frame_saida = ttk.Frame()
label_saida = ttk.Label(frame_saida,text="Saida", font=(None, 20))
combo_saida = ttk.Combobox(frame_saida,values= values, font=(None, 20))
combo_saida.set("en")

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column= 1, padx = 30, pady= 10)
frame_saida.pack()
saida = Text(height=10, width=50, font=(None,15), state='disabled')
saida.pack(padx =10, pady=20 ,fill='both', expand='yes')


#Botão
botao = Button(text="Traduzir",font=(None,20), bg="#070707", fg="#ffffff", command=traduzir) 
botao.pack(fill = 'both', pady=10, padx=10,)

janela.bind('<Return>', traduzir)

janela.mainloop()
