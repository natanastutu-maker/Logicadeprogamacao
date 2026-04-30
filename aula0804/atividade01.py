'''
Desenvolva um sistema que receba:
nome do usuário, data de nascimento, peso e altura
Formate a saída para aparecer na tela do usuário: 
"Olá (nome), seja bem vindo ao sistema Python!
Aqui estão as suas informações
- Data Nascimento: 
- Altura: 
- Peso
'''

nome = input("Qual seu nome: ")
data = input ("Quando você nasceu: ")
peso = float (input ("O seu peso: "))
altura = float(input ("Qual sua altura: "))

print ("Olá",nome,", seja bem vindo ao sistema Python!")
print ("Aqui estão as suas informações:","\n")
print ("A data de seu nascimento: ",data,"\n")
print ("A sua altura é: ",altura,"\n")
print ("O seu peso é: ",peso,"\n")