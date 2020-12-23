class TransacaoInvalida(Exception):
    def __init__(self, saldo_atual, quantidade):
        super(TransacaoInvalida, self).__init__(f"Sua conta não tem R$ {quantidade}")
        self.quantidade = quantidade
        self.saldo_atual = saldo_atual

    def excesso(self):
        return self.quantidade - self.saldo_atual


try:
    raise TransacaoInvalida(10, 20)
except TransacaoInvalida as e:
    print(f"Você não tem saldo suficiente, falta R$ {e.excesso():.2f}")



