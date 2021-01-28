class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        print(f"{self._nome} foi ligado agora!")

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

