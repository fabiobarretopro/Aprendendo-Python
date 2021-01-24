class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produtos):
                    self.produtos.append(produtos)

    def lista_produtos(self):
                    for produto in self.produtos:
                                    print(produto.nome, produto.valor)
        
    def soma_total(self):

                    total = 0
                    for produto in self.produtos:
                                    total = total + produto.valor
                    print(total)


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor