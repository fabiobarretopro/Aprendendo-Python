try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    r = n1/n2
    print(r)
except ValueError as ve:
    print(f"{ve}: Erro de tipo")
except ZeroDivisionError as zde:
    print(f"{zde}: Não pode ser divisível por zero.")
finally:
    print("Finalizando...")