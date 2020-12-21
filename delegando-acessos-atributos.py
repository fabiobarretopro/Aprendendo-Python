class A:
    def fazer_algo(self):
        print("Fazendo algo!")

    def outro_metodo(self):
        print("Fazendo outro método!")

    def algum_metodo(self, nome):
        print(nome)


class B:
    def __init__(self):
        self.a = A()

    def fazer_algo(self):
        return self.a.fazer_algo()

    def outro_metodo(self):
        return self.a.outro_metodo()

    def __getattr__(self, nome):
        return getattr(self.a, nome)


c = B()
c.fazer_algo()
c.outro_metodo()
c.algum_metodo("Python")
