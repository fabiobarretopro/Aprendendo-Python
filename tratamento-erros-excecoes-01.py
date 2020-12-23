# Exception genérico
try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    r = n1/n2
    print(r)
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
finally:
    print("Finalizando...")