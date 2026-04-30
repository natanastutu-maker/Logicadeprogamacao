## Laço de Repetição "for"
## Usado quando se tem uma sequência finita, sabendo quantos números de repetições acontecerá
## Função "for in" vai buscar elementos em uma lista

frutas = ['melancia', 'abacaxi', 'melão', 'pera']
fruta = 'melancia'

num = int input("Digite um número para saber a sua tabuada: ")


for i in range(1, 11):
    print (f"{i} X {num} = {i * num}")

# Formatação: for range(inicio, tamanho, salto)

for i in range(1, 20, 2):
    print (i)

# for f in fruta:
    #print (frutas(0))