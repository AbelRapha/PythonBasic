import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.title("Cotação da Moeda")

#Ajustando as janelas para não deformarem
window.rowconfigure(0, weight=1) #weight=0 sem redirecionamento automático 1 de forma automática
window.columnconfigure([0,1],weight=1)

message = tk.Label(text="Sistema de busca de cotação de moedas", background="black", fg="white", width=35, height=5)
message.grid(row=0, column=0, columnspan=2, sticky="NSEW")

message2 = tk.Label(text="Selecione a moeda deseja")
message2.grid(row=1, column=0, pady=10)

dict_quotes = {
    'Dólar': 5.47,
    'Euro':6.68,
    'BTC': 100.000,
}

currencies = list(dict_quotes.keys())

currency = ttk.Combobox(window, values=currencies)
currency.grid(row=1, column=1)

def search_quote():
    type_currency = currency.get()
    currency_quote = dict_quotes.get(type_currency)
    quote_message = tk.Label(text='Cotaçao não encontrada', fg="white", bg="Green")
    quote_message.grid(row=3, column=0)
    if currency_quote:
        quote_message['text'] = f'Cotação do {type_currency} é de {currency_quote} reais'

button = tk.Button(text="Buscar Cotação", command= search_quote)
button.grid(row=2, column=1, pady=10)

message3 = tk.Label(text='Caso queira mais de 1 cotação ao mesmo tempo, digite uma moeda em cada linha')
message3.grid(row=4, column=0, columnspan=2)

message_box = tk.Text(width=10, height=5)
message_box.grid(row=5, column=0, sticky='NSWE')

def search_quotes():
    text = message_box.get("1.0", tk.END)
    list_currencies = text.split("\n")
    quote_message = list()
    for currency_type in list_currencies:
        quote = dict_quotes.get(currency_type)
        if quote:
            quote_message.append(f'{currency_type}: {quote}')
    message4 = tk.Label(text='\n'.join(quote_message), fg="white", bg="green")
    message4.grid(row=6, column=1)


mutiple_quotes_button = tk.Button(text= 'Buscar cotações', command= search_quotes)
mutiple_quotes_button.grid(row=5, column=1)

window.mainloop()