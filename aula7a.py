name = str(input("Digite seu nome completo: "))
print(f"MAIÚSCULAS: {name.upper()}\nMINÚSCULAS: {name.lower()}\nTOTAL DE LETRAS: {len(name)- name.count(' ')}")
name = name.split()
print(f"LETRAS NO PRIMEIRO NOME: {len((name[0]))}")
