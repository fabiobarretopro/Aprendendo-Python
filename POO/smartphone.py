from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f"{self._nome} não está ligado, não podemos conectar!"
            print(info)
            self.log_erro(info)
            return

        if self._ligado:
            erro = f"{self._nome} Estava ligado, acabamos de conectar!"
            print(erro)
            self.log_erro(erro)
            return

        info = f"{self._nome} já está conectado!"
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            erro = f"{self._nome} não está conectado!!"
            print(erro)
            self.log_erro(erro)
            return
        self._conectado = False
        info = f"{self._nome} foi desconectado com sucesso!!"
        print(info)
        self.log_info(info)





