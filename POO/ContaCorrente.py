from classe_conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super(ContaCorrente, self).__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente!")
            return
        self.saldo = self.saldo - valor
        self.detalhes()
