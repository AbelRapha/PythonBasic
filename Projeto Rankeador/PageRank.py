#Função de troca de elementos dentro da lista
def troca(b,c):
  return (c,b)

#função de ordenacao
def bubble_sort(a,crit):
  n = len(a)
  for j in range(1, n): #Estrutura de repeticao que controla quantas vezes a troca sera realizada de acordo com a dimensao de index
    for i in range(0,n-1):
      if (crit[i] < crit[i+1]): #Com o sinal de > o maior valor da lista fica para o final e com sinal < o maior valor da lista fica em primeiro na lista
        crit[i], crit[i+1] = troca(crit[i],crit[i+1]) #Troca de posicao se a condicao do if for satisfeita
        a[i],a[i+1] = troca(a[i],a[i+1]) #Atauliza na lista index de acordo com a ataulizacao do pagerank

  return (a,crit) 



pagerank = [4.7,5.4,3.1,10.2] #Valores a serem orfdenados de forma decrescente ou crescente de acordo com o sinal de > ou < da funcao bubble_sort()
index = [0,1,2,3] #numero das paginas  
print("Valores da lista:" , pagerank)
print("Ordem da posicao da lista pagerank: ",index)
index, pagerank = bubble_sort(index,pagerank)
print("Valores da lista:" , pagerank)
print("Ordem da posicao da lista pagerank: ",index)