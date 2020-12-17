def he(n):
    print(f"{help(n)}")
    while True:
        n = str(input("Função ou biblioteca > "))
        if n == "fim":
            print("Até logo!")
            break
        else:
            he(n)


funcao = str(input("Função ou biblioteca > "))
he(funcao)

