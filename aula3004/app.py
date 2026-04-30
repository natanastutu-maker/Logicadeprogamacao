nome1 = input ("Digite o primeiro nome completo:")
nome2 = input ("Digite o segundo nome completo: ")

part1 = nome1.split()
part2 = nome2.split()

# pegar o primeiro nome e sobrenome
primeiro_nome = part1(-1)
sobrenome1 = part1(0)

segundo_nome = part2(-1)
sobrenome2 = part2(0)

# concatenação
novo_nome1 = primeiro_nome + " " + sobrenome2
novo_nome2 = segundo_nome + " " + sobrenome1