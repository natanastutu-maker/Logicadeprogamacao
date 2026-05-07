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
    #CRIAR
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
   


        proximo_id += 1
         
    with open('cadastro.txt', "w") as arquivo:
        for f in carros:
            arquivo.write(+ '\n')
    print("Carro cadastrado com sucesso!")

 #LISTAR
    elif input_usuario == "2":
        if not carros:
            print("Nenhum carro cadastrado.")
    else:
         print("Carros cadastrados:")
    
    for carro in carros:
            with open('cadastro.txt', 'r') as arquivo:
                infor = arquivo.readlines()
                print (type (infor))
                print (infor)
    
    # ATUALIZAR
    elif input_usuario == '3':
        ...

    # DELETE
    elif input_usuario == '4':
        print('\n Lista de carros')
        print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
    
    # SAIR
    elif input_usuario == "0":
        print("Saindo do sistema...")
        break