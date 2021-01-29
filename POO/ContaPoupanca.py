from classe_conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente!")
            return
        self.saldo = self.saldo - valor
        self.detalhes()


