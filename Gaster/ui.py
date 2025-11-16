from view import View

class UI:
    __usuario = None 


    @classmethod
    def main(cls):
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # mostra o menu da aplicação
        UI.menu()

    @classmethod  
    def menu(cls):
        op = 0
        while True:
            if cls.__usuario == None: 
                # usuário não está logado
                op = UI.menu_visitante()
                if op == 3:
                    break #tem que colocar o break para quebrar o loop
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.__usuario["nome"] == "admin"
                # mensagem de bem-vindo
                print("IF Comércio Eletrônico 2025")
                print("Bem-vindo(a), " + cls.__usuario["nome"])
                # menu do usuário: admin ou cliente
                if admin: UI.menu_admin()
                else: UI.menu_cliente()

    @staticmethod
    def menu_visitante():
        print('Bem-Vindo ao nosso sistema de compra!')
        print('1 - Entrar na conta')
        print('2 - Cadastrar uma nova conta')
        print('3 - Sair')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            UI.entrar()
        elif opcao == 2:
            UI.cadastrar()
        elif opcao == 3:
            print("Saindo...")
        else:
            print('Opção inválida, tente novamente')

        return opcao
        
    

    @classmethod
    def entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")
    
    @staticmethod  
    def cadastrar():
        UI.cliente_inserir()


    @staticmethod  
    def menu_admin():
        while True: #para tirar o loop
            print("Clientes")
            print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
            print()
            print("Categoria")
            print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
            print()
            print("Produtos")
            print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir, 13-Reajuste")
            print()
            print("Vendas")
            print("14-Listar as vendas")
            print()
            print("15-Fim")

            op = int(input("Informe uma opção: "))

            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.reajustar_preco()
            if op == 14: UI.venda_listar()
            elif op == 15: 
                UI.usuario_sair()
                break
            else:
                print('Opção Inválida, tente novamente')

    @staticmethod  
    def menu_cliente():
        while True: #precisa colocar para nao ficar o loop 
            print("1-Listar Produtos")
            print("2-Inserir Produto no carrinho")
            print("3-Visualizar carrinho")
            print("4-Comprar carrinho")
            print("5-Listar minhas compras")
            print("6-Fim")
            
            op = int(input("Informe uma opção: "))

            if op == 1: UI.listar_produtos()
            if op == 2: UI.inserir_produtos()
            if op == 3: UI.visualizar_carrinho()
            if op == 4: UI.comprar_carrinho()
            if op == 5: UI.listar_minhas_compras()
            if op == 6: UI.usuario_sair()


    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

    # Funções cliente
    @staticmethod  
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o número de telefone: ")
        senha = input("Insira uma senha: ")
        View.cliente_inserir(nome, email, fone, senha)

    @staticmethod  
    def cliente_listar():
        for obj in View.cliente_listar(): print(obj)

    @staticmethod  
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o número de telefone: ")
        senha = input("Insira sua nova senha: ")
        View.cliente_atualizar(id, nome, email, fone, senha)

    @staticmethod  
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.cliente_excluir(id)



    # Fuções da Categoria
    @staticmethod
    def categoria_inserir():
        descricao = input("Infor a descrição dessa categoria: ")
        View.categoria_inserir(descricao)

    @staticmethod
    def categoria_listar():
        for obj in View.categoria_listar():print(obj)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição dessa categoria: ")
        View.categoria_atualizar(id, descricao)

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)

    # Funções do produto

    @staticmethod
    def produto_inserir():
        descricao = input("Informa a descrição desse produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria desse produto colocando o id referente: "))
        View.produto_inserir(descricao, preco, estoque, id_Categoria)

    @staticmethod
    def produto_listar():
        for obj in View.produto_listar():print(obj)

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informa a nova descrição desse produto: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o atual estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria atual desse produto colocando o id referente: "))
        View.produto_atualizar(id, descricao, preco, estoque, id_Categoria)

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.produto_excluir(id)

    @staticmethod
    def reajustar_preco():
        UI.produto_listar()
        porcentagem = float(input("Informe a porcentagem: "))
        View.reajustar_preco(porcentagem)

    # Funções da venda
    
    @staticmethod
    def venda_listar():
        View.chec_vendas()
        
    # Funções do cliente

    @classmethod
    def listar_produtos(cls):
        print("Veja os produtos")
        print()
        print(cls.__usuario)
        UI.produto_listar()
    
    @classmethod 
    def inserir_produtos(cls): #FALTA FAZER USANDO CLS
        venda = View.venda_existe(cls.__usuario["id"])
        UI.produto_listar()
        produto = int(input("Digite o id do produto: "))
        quantos = int(input("Digite quantos você quer: "))
        preco = View.achar_preco(produto)
        View.vendaitem_inserir(quantos, preco, venda, produto)

    @classmethod
    def visualizar_carrinho(cls):
        venda = View.venda_existente(cls.__usuario["id"])
        View.visualizar_carrinho(venda)

    @classmethod    
    def comprar_carrinho(cls):
        if UI.visualizar_carrinho() == None: return "Seu carrinho está vazio"
        pagamento = UI.opcao_pagar()
        View.comprar_carrinho(pagamento, cls.__usuario["id"])

    @staticmethod
    def opcao_pagar():
        print("1-Crédito")
        print("2-Débito")
        print("3-Pix")
        print("4-Voltar")
        print()
        pagar = int(input("Escolha uma opção de pagamento: "))
        forma = View.opcao_pagar(pagar)
        return forma

    @classmethod
    def listar_minhas_compras(cls):
        vendas = View.venda_feita(cls.__usuario["id"])
        View.listar_minhas_compras(vendas)
        

UI.main()