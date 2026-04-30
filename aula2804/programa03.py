#Sistema de Calculadora



while True:
    print (30*"-", "Calculadora", 30*"-")
    num1 = input (f'Digita um número.')
    num2 = input (f'Digite outro número')
    print ('1, Soma')
    print ('2, Subtração')
    print ('3, Multiplicação')
    print ('4, Divisão')
    opcao = input ('Digite a operação: (+, -, *, /)')
    match opcao:
        case '+':
                resultado = num1 + num2
                print (f'O resultado é:, {num1}, '+', )
                pass
        case '-':
              pass
        case '/':
              pass
        case '*':
              pass