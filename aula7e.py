def linha():
    print(60*"=")
linha()
frase = str(input("Escreva uma frase qualquer: ")).upper()
print(f"{frase}")
print(f"A letra 'A' aparece {frase.count('A')} vezes\nPRIMEIRA VEZ NA POSIÇÃO {frase.find('A')}º\nÚLTIMA VEZ NA POSIÇÃO: {frase.rfind('A')}º"), linha()
