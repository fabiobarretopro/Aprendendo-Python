temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Continuar? [S/N]: ")).upper().strip()
    if resp in "N":
        break
print(len(princ))
print(f"Maior peso: {mai}, peso de", end=" ")
for p in princ:
    if p[1] == mai:
        print(p[0], end=" ")
print()
print(f"Menor peso: {men}, peso de", end=" ")
for p in princ:
    if p[1] == men:
        print(p[0], end=" ")
