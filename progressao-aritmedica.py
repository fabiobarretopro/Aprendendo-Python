pt = int(input("PRIMEIRO TERMO DA PA: "))
razao = int(input("RAZÃO DA PA: "))
print(f"{pt}", end="=> ")
for c in range(0, 9):
    pt = pt + razao
    print(f"{pt}", end="=> ")

