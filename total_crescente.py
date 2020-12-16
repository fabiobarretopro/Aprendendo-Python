resp = "S"
lista = []
totnum = 0
while resp == "S":
    num = int(input("Digite um valor: "))
    totnum = totnum + 1
    lista.append(num)
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break

ordem = sorted(lista)
desc = ordem[::-1]
print(f"Foram digitados {totnum} números.\nA lista na ordem decrescente: {desc}")
if 5 in lista: print(f"O valor 5 está na lista.")
else: print("O valor 5 não está na lista.")
