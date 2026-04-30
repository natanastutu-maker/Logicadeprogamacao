'''
Cálculos e manipulação de variáveis
'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite sua peso: ")
altura = input("Digite sua altura: ")

# tratamento de exceção (try, except)
try:
    idade = int(idade)
    peso = float (peso)
    altura = float (altura)
except ValueError as e:
    print(e)
imc = peso/(altura**2)

print ("Seu IMC é: ",imc)