from datetime import datetime
pessoa = dict()
pessoa["nome"] = str(input("Nome: "))
pessoa["ano_nasc"] = int(input("Ano de nascimento: "))
pessoa["ctps"] = int(input("Número: Caso não tenha = 0 "))
pessoa["idade"] = datetime.now().year - pessoa["ano_nasc"]

if pessoa["ctps"] != 0:
    pessoa["ano_contratação"] = int(input("Qual ano de contratação? "))
    pessoa["salário"] = int(input("Salário: R$ "))

pessoa["aposentar"] = pessoa["idade"] + 35

print(pessoa)
for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
