# Sistema de sorteio usando "random"

import os
import random

lista_nomes = ["Gerisvaldo da Silva", "Shaoulin Matador de Porco", 
"Matador de Calango",  "Aeronauta Barata",
"Agrícola Beterraba Areia","Agrícola da Terra Fonseca" ,"Alce Barbuda", 
"Amado Amoroso", "Amável de Sousa" ,"Amazonas Rio do Brasil Pimpão", 
"América do Sul Brasil de Santana", "Amin Amou Amado", "Antonio Manso", "Antonio Manso Pacífico de Oliveira Sossegado",
"Antônio Morrendo das Dores",
"Aricléia Café Chá",
"Asteróide Silverio",
"Aveia Cozida",
"Bandeirante do Brasil Paulistano",
"Barrigudinha Seleida",
"Bispo de Paris", 
"Bizarro Assada",
"Céu Azul do Sol Poente",
"Chevrolet da Silva Ford"
"Colápso Cardíaco da Silva",
"Disney Chaplin Milhomem da Silva",
"Dezêncio Feverêncio de Oitenta e Cinco",
"Dolores Fuertes de Barriga",
"Esparadrapo Clemente de Sá",
"Homem Bom da Cunha Souto Maior",
"Ilegível Inilegível",
"Inocêncio Coitadinho",
"Janeiro Fevereiro de Março Abril",
"Lança Perfume Rodometálico de Andrade", "Marciano Verdinho das Antenas Longas",
"Maria Privada de Jesus", "Maria Tributina Padeira Cataerva","Maria-você-me-mata",
"Mimaré Índio Brazileiro de Campos","Napoleão Sem Medo e Sem Mácula", "Natal Carnaval",
"Necrotério Pereira da Silva",
"Oceâno Atlântico Linhares",
"Otávio Bundasseca",
"Pacífico Armando Guerra Padre", "Filho do Espírito Santo Amém", 
"Plácido e Seus Companheiros","Remédio Amargo",
"Renato Pordeus Furtado", "Restos Mortais de Catarina","Rocambole Simionato"]

nome_sorteado = random.choice(lista_nomes)

lista_sorteados = []

sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice (lista_nomes)
    print (f'Sorteado: {nome_sorteado}')
    lista_sorteados.append (nome_sorteado)
    lista_nomes.remove (nome_sorteado)

    print (f'Lista antes de remover {len (lista_nomes)}')

    print (f'Lista atualizada {len (lista_nomes)}')
    sorteados +=1
print ("Fim do programa.")
