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



def  excluir_produto(): #função para excluir um produto
     print("Excluindo produto...\n")
     nome_exclusao = input("Nome do produto: ")
    
     for produto in produtos:
          if produto["nome"] == nome_exclusao:
               print(f"\n Produto encontrado: {produto["nome"]} - Quantidade atual {produto["quantidade"]} ")

               print("\nSelecione a ação que deseja tomar:")
               print("1 - Remover todo o estoque do produto")
               print("2 - Remover x quantidade do produto")

               opcao_remocao = int(input("Selecione uma opção: "))

               if opcao_remocao == 1:
                   responsavel = (input("Informe o nome do responsável pela ação: "))
                   produtos.remove(produto)
                   print(f"Produto {nome_exclusao} removido completamente por {responsavel}")
               elif opcao_remocao == 2:
                    quantidade_remover = int(input("Seleciona a quantidade que deseja remover: "))
                    if quantidade_remover <= produto["quantidade"]:
                         produto["quantidade"] = produto["quantidade"] - quantidade_remover
                         responsavel = input(f"Nome do responsável pela remoção: ")
                         print(f"Foram removidas {quantidade_remover} unidade(s) de {produto["nome"]}")
                         print(f"Quantidade restante: {produto["quantidade"]}")

                         if produto["quantidade"] == 0:
                              remover = input("Quantidade chegou a 0. Informe se deseja remover produto do sistema [s/n]: ")
                              if remover == "s":
                                   produtos.remove(produto)
                                   print(f"O produto {produto["nome"]} foi removido do sistema com sucesso!")
                    else:
                         print(f"Quantidade insuficiente! Quantidade disponível: {produto["quantidade"]}.")
               else:
                    print("Opção inválida")
               return
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

     opcao = (input("Escolha a opção: "))

     if opcao == "1":
         nome = input("Nome: ")
         data = input("Data: ")
         quantidade = int(input("Quantidade: "))
         responsavel = input("Nome do responsável pela ação: ")
         adicionar_produto(nome, data, quantidade, responsavel)
         print(f"Produto adicionado com sucesso por {responsavel}")
         #vai adicionar
     elif opcao == "2":
         excluir_produto()
         #vai excluir

     elif opcao == "3":
         listar_produtos()
         
     elif opcao == "4":
         print("Saindo...")
         #vai sair
         break
     else:
         print("Opção Inválida!")