# NOTE: Boletim Escolar

import os

os.system("cls")

nome = input("Digite o nome do aluno: ").title()
turma = input ("Digite a sua turma: ").upper()
nota1 = input ("Diga a primeira nota: ").replace(",",".")
nota2 = input ("Diga a segunda nota: ").replace(",",".")
nota3 = input ("Diga a terceira nota: ").replace(",",".")
nota4 = input ("Diga a quarta nota: ").replace(",",".")
nota5 = input ("Diga a quinta nota do aluno: ").replace(",",".")

try:
    nota1 = float (nota1)
    nota2 = float (nota2)
    nota3 = float (nota3)
    nota4 = float (nota4)
    nota5 = float (nota5)
except ValueError as e:
    print(e)

resultado = None


media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

if media >= 7:
    resultado = "Aprovado"
elif media >=5: 
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

os.system("cls")
print (30*"=","Boletim Escolar",30*"=")
print ("Nome do Aluno:", nome, " | Turma: ",turma)
print ("Nota1: ",nota1)
print ("Nota2: ",nota2)
print ("Nota3: ",nota3)
print ("Nota4: ",nota4)
print ("Nota5: ",nota5)

print (f"A média é: {media:.2f}")
print ("A situação: ",resultado)
