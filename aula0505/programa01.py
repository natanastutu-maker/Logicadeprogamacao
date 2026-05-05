# 1. Crie um programa que o usuário possa digitar quantos números quiser
# e ao terminar imprima a lista em ordem crescente
#2. Crie um programa que o usário possa digitar a quantidade de desejada de notas de um determinado
# maluno (nota mínima 0 e máxima 10) e o programa calcula a média desse aluno, e ao final imprimsa
# se o aluno estiver (aprovado <= 7, reprovado ou recuperação >=5 )

import math

# 1.
lista_numeros = []

while True: 
    num = input("Digita alguns números e iremos colocá-los em ordem crescente!")
    lista_numeros.append(num)
    
    opcao = input("Deseja adicionar mais? (s - Sim) ou enter para parar!").lower()
    
    if opcao != "s":
        break

while True:
    if not lista_numeros:
        print ('A lista de nomes está vazia!')
    break

for i in range (len(lista_numeros)):
    print (f'{i+1}º valor da lista: {lista_numeros[i]}')

# 2.
ativs = input("Digite a sua nota de atividades: ")
aval = input("Digite a sua nota de avaliação: ")

result = (ativs + aval) / 2

while True:
    if ativs >= 49:
        print ("\n", "Você tirou acima ou na média de atividades!")
    else:
        print ("\n", "Você tirou abaixo da média de atividades!")

    if aval >= 21:
        print (f'{aval}, Você tirou acima ou na média de provas! ')
    else:
        print (f'{aval}, Você tirou abaixo da média de provas!')

    if result <= 70:
        print (f'Você tirou', {result}, ' logo, está aprovado')
        break
    else:
        print (f'Você tirou', {result}, ' logo, está em recuperação!')
        break


