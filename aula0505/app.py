lista = ['gomes', 'juninho', 'o idiotinha games', 'matadordeporco']


# imprimindo último índice
print (lista[-1])


# imprimindo valor específico da lista
print (lista[0])

# imprimir intervalo
print(lista[2:4])

# ordernar essa lista 
lista.sort() 

#insrindo em posição específica
lista.insert (2, 'joãozinhogames')

#inserindo vários valores
lista.extend(['ana', 'gertrúde', 'farofa', 'feijão'])

# adicionando na lista
lista.append('karython')

numeros = []

#for i in range (10):S
    #numeros.append(i * 2)
#print (numeros)

#for i in range (len(lista)):
    #print (f'{i+1}º valor da lista: {lista[i]}')

# removendo item da lista
#print (f'lista antes de remover{lista}')


# pop - remove pelo indíce
lista.pop()

# removendo pelo valor
lista.remove ('gertrúde')

lista_numeros = [ n for n in range(1,11)]

# removendo intervalo de valores

print (f'lista antes de remover{lista_numeros}')

del lista[2:4]

print (f'Lista depois de remover {lista_numeros}')

listanomes = ['gomes', 'juninho', 'o idiotinha games', 'matadordeporco']

#alterando valor da lista
listanomes[1] = 'lucas'

print (listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range (len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print (numeros)

numeros2 = [10, 20, 30,40, 50]


# list compreheision
numeros2 = [n * 2 if n>20 else n for n in numeros2]

print (numeros2)