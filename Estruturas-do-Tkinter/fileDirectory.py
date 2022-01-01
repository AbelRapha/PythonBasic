from tkinter.filedialog import askopenfilename

directory_archive = askopenfilename(title="Selecione o arquivo")

arquivo = open(directory_archive, "r")
i = 0
for linha in arquivo:
    print(linha.strip())
    i+=1
print(i)