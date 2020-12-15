l1 = int(input(f"1º LADO: "))
l2 = int(input(f"2º LADO: "))
l3 = int(input(f"3º LADO: "))

if (l2 + l3) > l1 > (l2 - l3) and (l1 + l3) > l2 > (l1 - l3) and (l2 + l1) > l3 > (l2 - l1):
    print("FORMAM UM TRIÂNGULO!")
else:
    print("NÃO FORMAM UM TRIÂNGULO!")