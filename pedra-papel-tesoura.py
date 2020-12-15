import random
lista = ['PEDRA', "PAPEL", "TESOURA"]
jogador = str(input("Escolha pedra, papel ou tesoura: ")).upper()
computador = random.choice(lista)
if jogador == "PEDRA" and computador == "TESOURA" or jogador == "TESOURA" and computador == "PAPEL" or jogador == "PAPEL" and computador == "PEDRA":
    print(f"O jogador venceu! Ele escolheu {jogador} e o computador {computador}")
elif computador == "PEDRA" and jogador == "TESOURA" or computador == "TESOURA" and jogador == "PAPEL" or computador == "PAPEL" and jogador == "PEDRA":
    print(f"O computador venceu! Ele escolheu {computador} e o jogador {jogador}")
else:
    print(f"EMPATE! Jogador escolheu {jogador} e computador escolheu {computador}")


