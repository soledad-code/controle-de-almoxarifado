produtos = [] #lista vazia com os produtos a serem adicionados

def adicionar_produto(nome, data, quantidade, responsavel): #função de adicionar um produto
        print("Adicionando produto...\n")
        for produto in produtos:
             if produto["nome"] == nome:
                  produto["quantidade"] = produto["quantidade"] + quantidade
                  print(f"A quantidade de {produto["nome"]} foi atualizada para {produto["quantidade"]}")
                  return
        
        novo_produto = { #dicionario para colocar as características do produto
              "nome": nome,
              "data": data,
              "quantidade": quantidade,
              "responsavel": responsavel
        }
        produtos.append(novo_produto)
        print(f"{nome} adicionado com sucesso!")



def excluir_produto(): #função para excluir um produto
    print("Excluindo produto...\n")
    produto_exclusao = input("Nome: ")
    encontrado = False

    for produto in produtos:
        if produto["nome"] == produto_exclusao:
            responsavel = input("Nome do responsável pela ação: ") #registro do nome de quem realizou a exclusão
            produtos.remove(produto)
            encontrado = True
            print(f"Produto removido com sucesso por {responsavel}!")
            break
        
    if encontrado == False:
        print("Produto não encontrado!")

def listar_produtos(): #Listando os produtos atuais do almoxarifado
     print(" --- PRODUTOS CADASTRADOS ---")
     for produto in produtos:
        print(f"{produto['nome']} ({produto['data']}) - {produto['quantidade']} unidades. ADICIONADO POR {produto['responsavel']}")

        
while True: #MENU DO PROGRAMA EM LOOP
    print("--- CONTROLE DE ALMOXARIFADO ---\n")
    print("- Qual ação deseja tomar? -\n")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Sair")

    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
         nome = input("Nome: ")
         data = input("Data: ")
         quantidade = int(input("Quantidade: "))
         responsavel = input("Nome do responsável pela ação: ")
         adicionar_produto(nome, data, quantidade, responsavel)
         print(f"Produto adicionado com sucesso por {responsavel}")
         #vai adicionar
    elif opcao == 2:
         excluir_produto()
         #vai excluir

    elif opcao == 3:
         listar_produtos()
         
    elif opcao == 4:
         print("Saindo...")
         #vai sair
         break
    else:
         print("Opção Inválida!")