print(f"{'BANCO FÁBIO BARRETO':=^30}")
print(f"{'CAIXA ELETRÔNICO':=^30}")
valor = int(input("QUAL VALOR A SER SACADO? "))  # CÉDULAS DE 50 20 10 1
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R$ {ced}")
        if ced == 50:
            dec = 20
        elif ced == 20:
            dec = 10
        elif ced == 10:
            dec = 1
        totced = 0
        if total == 0:
            break
