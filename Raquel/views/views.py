from models.cliente import Cliente, ClienteDAO
from models.produto import Produto, ProdutoDAO
from models.categoria import Categoria, CategoriaDAO 


class View:


    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_inserir(nome: str, email: str, fone:str):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c) #nao tem return, porque esta inserindo, do qual nao precisa mostrar 

    def cliente_atualizar(id: int, nome: str, email:str, fone:str):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    def cliente_excluir(id:int):
        c = Cliente(id, '','','','') #somente o id para excluir
        ClienteDAO.excluir(c)
    
    def categoria_listar():
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str):
        c = Categoria(0, descricao)  #nao tem problema colocar id depois, mas sempre deve colocar
        CategoriaDAO.inserir(c)

    def categoria_atualizar(id: int, descricao: str):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)

    def categoria_excluir(id: int):
        c = Categoria(id, '')
        CategoriaDAO.excluir(c)

    def produto_listar():
        return ProdutoDAO.listar()

    def produto_inserir(descricao: str, preco: float, estoque: int, idCategoria: int):
        p = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO.inserir(p)

    def produto_atualizar(id: int, descricao: str, preco: float, estoque: int, idCategoria: int):
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(p)
        
    def produto_excluir(id: int):
        p = Produto(id, '', '', '', '')
        Produto.excluir(p)
        
    def produto_reajustar(percentual: float):
        for obj in ProdutoDAO.listar():
            obj.reajustar()
            ProdutoDAO.atualizar(obj)
    

    
