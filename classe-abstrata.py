def numeros(func):
    def depurando(*args):
        print(f"Passando {args}")
        return func(*args)
    return depurando


@numeros
def somar(a, b):
    print(f"{a + b}")


@numeros
def multi(a, b):
    print(f"{a * b}")


somar(2, 3)
multi(2, 3)
