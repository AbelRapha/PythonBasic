import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import DateEntry
import requests as r

#Requests iin Awesome Api
api = r.get("http://127.0.0.1:5000/moedas")

def get_quote():
    pass

def get_archive():
    pass

def update_quote():
    pass

window  = tk.Tk()

#Ajustando as janelas para não deformarem
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], weight=1) #weight=0 sem redirecionamento automático 1 de forma automática
window.columnconfigure([0,1,2],weight=1)

window.title('Ferramenta de cotação de Moedas')

#Select just one one currency
label_quote_currency = tk.Label(text="Cotação de 1 única moeda " , bg="black", fg="white")
label_quote_currency.grid(row=0,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)

label_select_currency = tk.Label(text="Selecione a Moeda " , bg="blue", fg="black")
label_select_currency.grid(row=1,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)
#Select Currency
combobox_select_currency = ttk.Combobox(values=list_currencies)
combobox_select_currency.grid(row=1, column=2, padx=10, pady=10, sticky="nswe")
#Select Data
label_select_currency = tk.Label(text="Selecione o dia da Cotação " , bg="blue", fg="black")
label_select_currency.grid(row=2,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)

#Select Data of quote
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
calendar_of_currency = DateEntry(year= date.year, locale='pt_br')
calendar_of_currency.grid(row=2,column=2, padx = 10, pady=10, sticky='nswe')

#Button
label_text_quote = tk.Label(text="")
label_text_quote.grid(row=3, column=0, columnspan=2, padx=2, pady=10, sticky="nswe")


button_get_quote = tk.Button(text="Buscar Cotação", command= get_quote, bg='green', fg='white')
button_get_quote.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

#Select Most Currencies
label_quote_most_currency = tk.Label(text="Cotação Vários tipos de Moedas " , bg="black", fg="white")
label_quote_most_currency.grid(row=4,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)

#Select Archive
label_select_archive = tk.Label(text="Selecione um arquivo com as moedas a serem buscadas. (EXTENSÕES ACEITAS: EXCEL, CSV)", bg='blue', fg='black')
label_select_archive.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

#Button Select Archive
button_select_archive = tk.Button(text="Clique para selecionar o arquivo", command=get_archive)
button_select_archive.grid(row=5, column=2, padx=10,pady=10,sticky='nswe')

#Label Selected Text
label_selected_text = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
label_selected_text.grid(row=6,column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

#Select Data Initial
label_select_currency_initial = tk.Label(text="Selecione o dia da Cotação Inicial" , bg="gray", fg="white")
label_select_currency_initial.grid(row=7,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)

#Select Data Final
label_select_currency_final = tk.Label(text="Selecione o dia da Cotação Final" , bg="gray", fg="white")
label_select_currency_final.grid(row=8,column=0, padx=10,pady=10, sticky="NSWE", columnspan=2)

#Select Data of quote Initial
calendar_of_currency_initial = DateEntry(year= date.year, locale='pt_br')
calendar_of_currency_initial.grid(row=7,column=2, padx = 10, pady=10, sticky='nswe')
#Select Data of quote Final
calendar_of_currency_final = DateEntry(year= date.year, locale='pt_br')
calendar_of_currency_final.grid(row=8,column=2, padx = 10, pady=10, sticky='nswe')

#button update quotes
button_update_quotes = tk.Button(text="Atualizar Cotação", command=update_quote, bg='green', fg='white')
button_update_quotes .grid(row=9, column=0, padx=10,pady=10,sticky='ns')

#Label Update quotes
label_update_quote = tk.Label(text="")
label_update_quote.grid(row=9, column=1, columnspan=2, padx=2, pady=10, sticky="nswe")


#Button Close Program
button_close_program = tk.Button(text="Fechar", command= window.quit, bg='red', fg='white')
button_close_program.grid(row=10, column=2, padx=10,pady=10,sticky='nswe')

window.mainloop()