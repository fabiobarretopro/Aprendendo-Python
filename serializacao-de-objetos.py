# Serializando objetos: JSON - Javascript Object Notation
import json


class Contato:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        print(f"{self.primeiro_nome} {self.sobrenome}")


c = Contato("Fábio", "Barreto")
print(json.dumps(c.__dict__))
