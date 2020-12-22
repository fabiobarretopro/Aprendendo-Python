class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)


p = Pessoa("Fábio")
print(p.nome)

p = Pessoa.outro_construtor("Maria Clara")
print(p.nome)

