import random
import os
import time
lista_nomes = []
print (30*"-", "Bem vindo ao sistema de Sorteios")

while True: 
    nome = input ("Digite um nome para ser sorteado: ").title()
    lista_nomes.append(nome)
    
    opcao = input ("Deseja adicionar mais? (s - Sim) ou enter para parar!").lower()
    
    if opcao != "s":
        break

while True:
    if not lista_nomes:
        print ('A lista de nomes está vazia!')
    break

else:
    nome_sorteado = random.choice(lista_nomes)
    lista_nomes.remove(nome_sorteado)
    lista_sorteados.append(nome_sorteado)
    os.system('cls')
    
    
    

for i in range(5, 0, -1):
    os.system('cls')
    time.sleep(1)
    print (f'Contagem regressiva' [i])
    i -=1
    
print ("O nome sorteado foi: ",[nome_sorteado])
 
sortear_novamente = input ('Deseja sortear outro nome? (s - Sim)| (n - Não)')
if sortear_novamente == nome:
    break