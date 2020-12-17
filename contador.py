from time import sleep


def contador(i, f, p):
        if i < f:
            print(f"Contagem de {i} até {f} de {p} em {p}")
            for c in range(i, f+1, p):
                print(f"{c}", end=", ")
                sleep(0.3)
            print("FIM!")
            print("="*40)
        if i > f:
            if p > 0:
                print(f"Contagem de {i} até {f} de {abs(p)} em {abs(p)}")
                for c in range(i, f-1, -p):
                    print(f"{c}", end=", ")
                    sleep(0.3)
                print("FIM!")
                print("=" * 40)
            if p < 0:
                print(f"Contagem de {i} até {f} de {abs(p)} em {abs(p)}")
                for c in range(i, f - 1, p):
                    print(f"{c}", end=", ")
                    sleep(0.3)
                print("FIM!")
                print("=" * 40)
            elif p == 0:
                print(f"Contagem de {i} até {f} de {abs(-1)} em {abs(-1)}")
                for c in range(i, f - 1, -1):
                    print(f"{c}", end=", ")
                    sleep(0.3)
                print("FIM!")
                print("=" * 40)


# Programa principal:


contador(1, 10, 1)
contador(10, 0, -2)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)





