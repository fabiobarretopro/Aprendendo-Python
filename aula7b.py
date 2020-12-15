num = int(input("Digite um número inteiro de 0 a 9999:"))
unidade = num%10
dezena = num%100//10
centena = num%1000//100
milhar = num//1000
print(f"UNIDADE: {unidade}\nDEZENA: {dezena}\nCENTENA: {centena}\nMILHAR: {milhar}")