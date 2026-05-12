# DEFINIÇÃO DE FUNÇÃO
#def funcao_segundo_grau(a,b,c):
    #print ("Olá, mundo!")
    #return a,b,c

#x = funcao_segundo_grau(1,2,3)

#print(x)

# FUNÇÃO COM PARÂMETRO
def funcao_segundo_grau(a,b,c):
    return a, b , c

# #CHAMANDO A FUNÇÃO E ARMAZENANDO O VALOR EM UMA VARIÁVEL
# x = funcao_segundo_grau(1,2,3)
# print (x)

# def soma(a,b):
#     result = a + b
#     return result

# result = soma(10,10)
# print (result)

# num1 = int(input("Digite um número ae mano"))
# num2 = int(input("Digita um número ai denovo paizão"))

# result = soma(num1, num2)
# print(result)

def mostrar_msg():
    print("ME AJUDA PORFAVOR")

mostrar_msg()

def mostrar_saud(nome):
    print(f'NÃO AJUDA {nome} NÃO, NÃO AJUDA')

mostrar_saud('Nat').title()

# FUNÇÃO RECURSIVA
def fatorial (n):
    #n!
    return 1 if n == 0 else n * fatorial (n-1)
