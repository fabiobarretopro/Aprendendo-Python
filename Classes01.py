class MinhaClasse(object):
    pass


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf


p1 = Pessoa("Marcos", 28)
print(p1.nome)
print(p1.idade)

p2 = PessoaFisica(123456, "Maria", 5)
print(p2.cpf)
print(p2.nome)
print(p2.idade)
