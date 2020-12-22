class SomentePares(list):
    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError("Somente inteiros")
        if inteiro % 2 != 0:
            raise ValueError("Somente Pares")
        super(SomentePares, self).append(inteiro)


sp = SomentePares()
sp.append(10)
sp.append(30)
sp.append(4)
print(sp)
