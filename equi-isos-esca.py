l1 = int(input(f"Digite um lado l1 do triângulo:"))
l2 = int(input(f"Digite um lado l2 do triângulo:"))
l3 = int(input(f"Digite um lado l3 do triângulo:"))

if l2 - l3 < l1 < l2 + l3 and l1 - l3 < l2 < l1 + l3 and l2 - l1 < l3 < l2 + l1:
    print("É um triângulo!")
    if l1 == l2 == l3:
        print("Triângulo equilátero!")
    elif l1 == l2 or l1 == l3 or l1 == l3:
        print("Triângulo Isósceles!")
    else:
        print("Triângulo Escaleno!")
else:
    print("Não é um triângulo!")