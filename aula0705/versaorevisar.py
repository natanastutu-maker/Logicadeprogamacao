import time
#cadastrar

carros = []
proximo_id = 1
while True:
    print("============ MENU ===========")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. editar carro")
    print("4. Excluir carro")
    print("0. Sair")
    input_usuario = input("Digite a opção desejada: ")
    #criar
    if input_usuario == "1":
        marca = input("Digite a marca do carro: ").title()
        preço = float(input("Digite o preço do carro: "))
        modelo = input("Digite o modelo do carro: ").title()

        carro = {
            "id": proximo_id,
            "marca": marca,
            "preço": preço,
            "modelo": modelo
        }
        
        carros.append(carro)
        proximo_id += 1
        print("Carro cadastrado com sucesso!")
        with open("carros.txt", "w") as arquivo:
            for carro in carros:
                arquivo.write(str(carro) + "\n")

    #lista de carros
    elif input_usuario == "2":
        arquivo = open("carros.txt", "r")
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("Carros cadastrados:")
            for carro in carros:
                print(f"ID: {carro['id']}, Marca: {carro['marca']}, Preço: R${carro['preço']:.2f}, Modelo: {carro['modelo']}")
      
    #editar
    elif input_usuario == "3":
        id_carro = int(input("Digite o ID do carro a editar: "))
        for carro in carros:
            if carro['id'] == id_carro:
                carro['marca'] = input("Digite a nova marca do carro: ").title()
                carro['preço'] = float(input("Digite o novo preço do carro: "))
                carro['modelo'] = input("Digite o novo modelo do carro: ").title()
                print("Carro editado com sucesso!")
                break
       
            print("Carro não encontrado.")
    elif input_usuario == "4":
        id_carro = int(input("Digite o ID do carro a excluir: "))
        for i, carro in enumerate(carros):
            if carro['id'] == id_carro:
                carros.pop(i)
                print("Carro excluído com sucesso!")
                break
        else:
            print("Carro não encontrado.")
    elif input_usuario == "0":


        #sair do programa
        print("Saindo do programa...")
        time.sleep(2)

        break
    else:
        print("Opção inválida.")