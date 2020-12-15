import random
# =================================
def linha():
    print(30*"=+")
linha()
comp = random.randint(0, 5)
usua = int(input("Tente adivinhar o número do computador (1 a 5): "))
if usua == comp:
    print(f"Você venceu!! Você escolheu {usua} e o computador {comp}")
else:
    print(f"Você perdeu! Você escolheu {usua} e o computador {comp}")
linha()