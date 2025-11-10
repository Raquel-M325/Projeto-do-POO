from view import View

class UI:
    
    def menu():
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print()
        print("Categoria")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print()
        print("Produtos")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir, 13-Reajuste")
        print()
        print("13-Fim")
        return int(input("Informe uma opção: "))
    
    def main():
        op = 0
        while op != 14:
            op = UI.menu()
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

    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o número de telefone: ")
        View.cliente_inserir(nome, email, fone)

    def cliente_listar():
        for obj in View.cliente_listar():print(obj)

    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o número de telefone: ")
        View.cliente_atualizar(id, nome, email, fone)

    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.cliente_excluir(id)

    def categoria_inserir():
        descricao = input("Infor a descrição dessa categoria: ")
        View.categoria_inserir(descricao)

    def categoria_listar():
        for obj in View.categoria_listar():print(obj)

    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição dessa categoria: ")
        View.categoria_atualizar(id, descricao)

    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)

    def produto_inserir():
        descricao = input("Informa a descrição desse produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria desse produto colocando o id referente: "))
        View.produto_inserir(descricao, preco, estoque, id_Categoria)

    def produto_listar():
        for obj in View.produto_listar():print(obj)

    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informa a nova descrição desse produto: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o atual estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria atual desse produto colocando o id referente: "))
        View.produto_atualizar(id, descricao, preco, estoque, id_Categoria)

    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))

    def reajustar_preco():
        UI.produto_listar()
        porcentagem = int(input("Informe a porcentagem: "))
        View.reajustar_preco(porcentagem)

UI.main()