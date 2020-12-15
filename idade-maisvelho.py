l_name = []
l_age = []
l_sex = []
l_fem = []
soma = media = mv = 0
for c in range(0, 4):
    name = str(input("NAME: ")).upper().strip()
    l_name.append((name))
    age = int(input("IDADE: "))
    soma = soma + age
    media = soma/4
    l_age.append(age)
    mv = max(l_age)
    sex = str(input("SEXO: [M/F]")).upper().strip()
    
    l_sex.append(sex)


print(f"A média de idade do grupo é de {media} anos\nO homem mais velho tem {mv} anos.")

