media = soma = totnum = 0
lista = []
resp = "S"
while resp == "S":
    num = int(input("Digite um número inteiro: "))
    resp = str(input("Quer continuar a digitar os valores? [S/M]")).upper().strip()
    totnum = totnum + 1
    soma = soma + num
    media = soma/totnum
    lista.append(num)
    ma = max(lista)
    me = min(lista)
print(f"A média entre os números é {media}\nO maior valor: {ma}\nO menor valor: {me}")
print("Programa finalizado.")
