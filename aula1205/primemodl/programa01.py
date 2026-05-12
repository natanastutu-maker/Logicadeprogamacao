# Pré Modularização de Sistema
import modulo as ma

# Definição de módulo como principal, fórmula para executar esse e mais outros módulos
if __name__ == "__main__":
    while True:
        print ("Calculadora")
        print ("1. Somar")
        print ("2. Subrair")
        print ("3. Multiplicar")
        print ("4. Dividir")
        print ("5. Limpar Terminal")

        option = input("Digite a opção desejada: ")

        match option:
            case "1":
                print ('------ SOMA -------')
                num1 = int (input ('Digite um número para somar: '))
                num2 = int (input('Digite um número ai pra somar também: '))

                resze = ma.soma(num1, num2)
                print (f'Resultado = {resze}')
            case "2":
                print ("----- SUBTRAÇÃO ------")
                num1 = int (input ('Digite um número para subtrair: '))
                num2 = int (input('Digite um número ai pra subtrair também: '))
                resze = ma.subtracao(num1, num2)
                print (f'Resultado = {resze}')
            case "3":
                print ("----- MULTIPLICAÇÃO -----")
                num1 = int (input ('Digite um número para multiplicar: '))
                num2 = int (input('Digite um número ai pra multiplicar também: '))
                resze = ma.multiplicaçao(num1, num2)
                print (f' Resultado = {resze}')
            case "4":
                print ("----- DIVISÃO ----- ")
                num1 = int (input ('Digite um número para dividir: '))
                num2 = int (input('Digite um número ai pra dividir também: '))
            case "5":
                ma.limpa_terminal()
                break
            case _ :
                print ("Opção inválida!")


       
