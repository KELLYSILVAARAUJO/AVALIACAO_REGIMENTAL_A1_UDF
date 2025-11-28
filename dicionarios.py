def sistema_cadastro_produtos():
    # O dicionário 'produtos' usará o NOME do produto como CHAVE e o PREÇO do produto como VALOR.
    produtos = dict()
    
    print("🛒 Sistema de Cadastro de Produtos")
    
    # Inserção de Dados (Função para coletar nome e preço e armazenar no dicionário.)
    def inserir_produto():

        print("\n--- Inserir Novo Produto ---")
        
        while True:
            nome = input("Digite o NOME do produto: ").strip().capitalize()
            if nome:
                break
            print("O nome do produto não pode ser vazio.")

        while True:
            try:
                preco_str = input(f"Digite o PREÇO de {nome}: R$ ")
    # Garante que o preço seja um número positivo (ou zero)
                preco = float(preco_str.replace(',', '.')) 
                if preco >= 0:
                    break
                print("O preço deve ser um valor positivo.")
            except ValueError:
                print("Preço inválido. Digite um número.")

    # Armazena o produto: Chave é o nome, Valor é o preço
        produtos[nome] = preco
        print(f"Produto '{nome}' cadastrado com sucesso! Preço: R$ {preco:.2f}")

    # Recuperação de Dados (Função)
    def listar_produtos():
        """Função para exibir todos os produtos cadastrados."""
        print("\n--- Lista de Produtos Cadastrados ---")
        
        if not produtos:
            print("Nenhum produto cadastrado no momento.")
            return

    # Itera sobre o dicionário para exibir as chaves (nomes) e valores (preços); Usamos .items() para acessar chave (nome) e valor (preco) ao mesmo tempo.
        for nome, preco in produtos.items():
            print(f"- **{nome}**: R$ {preco:.2f}")
            
        print(f"\nTotal de produtos únicos cadastrados: {len(produtos)}")

    # Menu Principal
    while True:
        print("\n--- Menu ---")
        print("1. Inserir Produto")
        print("2. Listar Todos os Produtos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == '1':
            inserir_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            print("\n👋 Obrigado por usar o sistema! Encerrando...")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Execução do sistema
sistema_cadastro_produtos()