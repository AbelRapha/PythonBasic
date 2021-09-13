#Utilizando Dicionários

salario  = float(input("Digite seu Salário Bruto: "))

faixaDeDesconto = {0: 0.0,
                   1: 7.5,
                   2: 15,
                   3: 22.5,
                   4: 27.5}
faixaDeDeducao = {0: 0.0,
                  1: 142.80,
                  2: 354.80,
                  3: 636.13,
                  4: 869.36 }    
#Condições lógicas para verificar em qual faixa cada pessoa irá se encaixar de acordo com o salário bruto

if (salario <= 1903.98):
  faixa = 0
elif (salario > 1903.98) and (salario <= 2826.65):
  faixa = 1 
elif (salario > 2826.65) and (salario <= 3751.05):
  faixa = 2  
elif (salario > 3751.05) and (salario <= 4664.68):
  faixa = 3
else:
  faixa = 4       

#Cálculo do Imposto

imposto = salario * (faixaDeDesconto[faixa]/100)

valorPadrao = faixaDeDeducao[faixa]

impostoAPagar = imposto - valorPadrao

liquido = salario - impostoAPagar

#Criacao das mensagens para apresentar ao usuario

mensagem1 = "Bruto : %10.2f, Faixa: %d, Imposto: %5.2f"%(salario,faixa,imposto)

mensagem2 = "Padrão : %5.2f, A pagar : %5.2f, Liquido: %5.2f "%(valorPadrao, impostoAPagar, liquido)

print(mensagem1)
print(mensagem2)