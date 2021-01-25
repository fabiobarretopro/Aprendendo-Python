from composição import Cliente

c1 = Cliente("Fábio", 40)
c1.insere_endereco("Salvador", "BA")
print(c1.nome)
c1.lista_enderecos()
del c1
print("===============================================")
c2 = Cliente("Maria Clara", 5)
c2.insere_endereco("Lauro de Freitas", "BA")
c2.insere_endereco("Salvador", "BA")
print(c2.nome)
c2.lista_enderecos()
del c2
print("===============================================")
c3 = Cliente("Ana Júlia", 32)
c3.insere_endereco("Feira de Santana", "BA")
print(c3.nome)
c3.lista_enderecos()
del c3
print("######################################################")
