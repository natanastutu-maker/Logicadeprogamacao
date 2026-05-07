# Manipulação de arquivos: percorrer diretórios -> encontrar o arquivo -> transmitir o comando
# de abertura de arquivo -> transmitir comando de ação

# arquivo = open('arquivo.txt', 'modo')

# modos de ação:
# - "r": leitura do arquivo
# - "w": escrita (obs: sobreescreve o conteúdo antigo)
# - "a": adiciona conteúdo
# - "x": criar um arquivo
# - "b": arquivos binários
# - "t": texto

arquivo = open('primeiro_arquivo.txt', 'w')
arquivo.write('Olá mundo!')
arquivo.close()

# lendo arquivo
arquivo = open('primeiro_arquivo.txt', 'r')
conteudo = arquivo.read()

print (conteudo)
arquivo.close()

# aplicando boa prática
# as = alias ou apelido 
# with = gerenciar o 
with open ("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print (conteudo)

# arquivo com múltiplas escritas
with open("alunos.txt", "w") as arquivo:
    arquivo.write('Anatel\n')
    arquivo.write('IBM\n')
    arquivo.write('JOÃOZINHOGAMES\n')
    arquivo.write('XAULINMATADORDECÓDIGOS\n')

# lendo linha a linha
with open('alunos.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever no arquivo
frutas = ['pera', 'abacaxi', 'melancia', 'manga', 'caju']

with open('frutas.txt', "w") as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

# converter o arquivo em uma lista
with open('frutas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print (type (linhas))
    print (linhas)

# Saida: ['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

#limpar a qubra de linha

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())


# exemplo para cadastro

while True:
    nome = input("Digite seu nome: ").title()
    with open("cadastro.txt", 'a') as arquivo:
        arquivo.write(nome + "\n")
    sair = input ("Deseja sair? s/n").lower()
    
    if sair == 's':
        break

