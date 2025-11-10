from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO

class UI:
    

    @staticmethod

    def main(): 



    def menu_visitante():
        print('Bem-Vindo ao nosso sistema de compra!')
        print('1 - Entrar na conta')
        print('2 - Cadastrar uma nova conta')
        print('3 - Sair')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            UI.entrar()
        
        if opcao == 2:
            UI.cadastrar()

        else:
            UI.menu_visitante()

    def cadastrar():
       UI.cliente_inserir()

    def entrar():
        email = print(input('Digite o seu email: ')) #tá incompleto
        senha = print(input('Digite a sua senha: '))
      

    def menu_cliente():

        

    def menu_adm():  #só adm é que poderá fazer isso
        print('Bem vindo ao nosso Sistema de Comércio Eletrônico!')
        print('Escolha o nosso MENU abaixo:')
        print('0 - Sair')
        print('==========CLIENTE==================')
        print('1 - listar clientes')
        print('2 - inserir cliente')
        print('3 - atualizar cliente')
        print('4 - excluir cliente')

        print('==========CATEGORIA==================')
        print('5 - listar categorias')
        print('6 - inserir categoria')
        print('7 - atualizar categoria')
        print('8 - excluir categoria')

        print('==========PRODUTO==================')
        print('9 - listar produtos')
        print('10 - inserir produto')
        print('11 - atualizar produto')
        print('12 - excluir produto')


    @staticmethod
    def menu():
        while True: #para ficar sempre perguntando até o usuário querer sair com 0
            UI.main()
            resposta = input('Digite qual opção deseja: ')
            if resposta == '1':
                UI.cliente_listar() 
            elif resposta == '2':
                UI.cliente_inserir()
            elif resposta == '3':
                UI.cliente_atualizar()
            elif resposta == '4':
                UI.cliente_excluir()
            elif resposta == '5':
                UI.categoria_listar()
            elif resposta == '6':
                UI.categoria_inserir()
            elif resposta == '7':
                UI.categoria_atualizar()
            elif resposta == '8':
                UI.categoria_excluir()
            elif resposta == '9':
                UI.produto_listar()
            elif resposta == '10':
                UI.produto_inserir()
            elif resposta == '11':
                UI.produto_atualizar()
            elif resposta == '12':
                UI.produto_excluir()
            elif resposta == '0':
                print('Saindo do sistema...')
                break
            else:
                print('Opção inválida! Tente novamente.')

    @staticmethod
    def produto_listar(): #quero ver se existe produtos
        produto = ProdutoDAO.listar()
        if not produto:
            print('Não há produto cadastrado')
        else:
            for p in produto:
                print(p) #chamando o __str__ da classe ProdutoDAO
        input("\nPressione Enter para voltar ao menu...")

    @staticmethod
    def produto_inserir():
        descricao = str(input('Descreva o produto: '))
        preco = float(input('Preço do produto: '))
        estoque = int(input('A quantidade do produto que está no estoque: '))
        categoria_id = int(input('Digite o ID da categoria do produto: '))
        
        produto = Produto(0, descricao, preco, estoque, CategoriaDAO.listar_id(categoria_id))
        
        ProdutoDAO.inserir(produto)
        print('Produto inserido com sucesso!')

    @staticmethod
    def produto_atualizar():
        id = int(input('Digite o ID produto: '))
        descricao = str(input('Digite nova descrição do produto: '))
        preco = float(input('Digite o novo preço do produto: '))
        estoque = int(input('Digite a nova quantidade do produto no estoque: '))
        categoria_id = int(input('Digite o ID da nova categoria do produto: '))

        produto = Produto(id, descricao, preco, estoque, CategoriaDAO.listar_id(categoria_id))

        ProdutoDAO.atualizar(produto)
        print('Produto atualizado com sucesso!')

    @staticmethod
    def produto_excluir():
        id = int(input('Digite o ID do produto que deseja excluir: '))
        produto = ProdutoDAO.listar_id(id)

        ProdutoDAO.excluir(produto)
        print('Produto excluído com sucesso!')

    @staticmethod
    def categoria_listar():
        categoria = CategoriaDAO.listar()
        if not categoria:
            print('Não há categoria cadastrada')
        else:
            for c in categoria:
                print(c) #chamando o __str__ da classe CategoriaDAO
        input("\nPressione Enter para voltar ao menu...")

    @staticmethod
    def categoria_inserir():
        descricao = str(input('Descreva a categoria: '))
        categoria = Categoria(0, descricao)
        
        CategoriaDAO.inserir(categoria)
        print('Categoria inserida com sucesso!')

    @staticmethod
    def categoria_atualizar():
        id = int(input('Digite o ID da categoria: '))
        descricao = str(input('Digite a nova descrição da categoria: '))

        categoria = Categoria(id, descricao)

        CategoriaDAO.atualizar(categoria)

        print('Categoria atualizada com sucesso!')
    
    @staticmethod
    def categoria_excluir():
        id = int(input('Digite o ID da categoria que deseja excluir: '))
        categoria = CategoriaDAO.listar_id(id)

        CategoriaDAO.excluir(categoria)
        print('Categoria excluída com sucesso!')

    @staticmethod
    def cliente_listar():
        cliente = ClienteDAO.listar()
        if not cliente:
            print('Não há cliente cadastrado')
        else:
            for c in cliente:
                print(c)  #chamando o __str__ da classe ClienteDAO
        input("\nPressione Enter para voltar ao menu...")

    @staticmethod
    def cliente_inserir():
        nome = str(input('Nome do cliente: '))
        email = str(input('Email do cliente: '))
        fone = str(input('Fone do cliente: '))

        cliente = Cliente(0, nome, email, fone)

        ClienteDAO.inserir(cliente)
        print('Cliente inserido com sucesso!')

    @staticmethod
    def cliente_atualizar():
        id = int(input('Digite o ID do cliente: '))
        nome = str(input('Digite o novo nome do cliente: '))
        email = str(input('Digite o novo email do cliente: '))
        fone = str(input('Digite o novo fone do cliente: '))

        cliente = Cliente(id, nome, email, fone)

        ClienteDAO.atualizar(cliente)
        print('Cliente atualizado com sucesso!')

    @staticmethod
    def cliente_excluir():
        id = int(input('Digite o ID do cliente que deseja excluir: '))
        cliente = ClienteDAO.listar_id(id)
        ClienteDAO.excluir(cliente)
        print('Cliente excluído com sucesso!')

if __name__ == '__main__':
    UI.menu()
