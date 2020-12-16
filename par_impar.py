import random
from math import floor
total = soma = 0
while True:
    a = str(input("Par ou ímpar? ")).upper().strip()
    n = a[0]
    com = random.random()*1000
    comp = floor(com)
    jog = int(input("Escolha um número qualquer: "))
    soma = jog + comp
    print(f"{soma}")
    if soma % 2 == 0 and n == "P" or soma % 2 != 0 and n == "I":
        print(f"Você venceu, escolheu {jog} e eu {comp} e a soma deu {soma}")
        total = total + 1
    elif soma % 2 == 0 and n == "I" or soma % 2 != 0 and n == "P":
        print(f"Você perdeu!!! Você escolheu {jog} e eu {comp} e a soma deu {soma}")
        break

print(f"Você obteve um total de {total} triunfos consecutivos.")