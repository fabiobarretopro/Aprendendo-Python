from herança import Cliente, Aluno

c1 = Cliente("Fábio", 40)
print(c1.nome, c1.idade)
c1.falar()
c1.comprar()

a1 = Aluno("Maria Clara", 5)
print(a1.nome, a1.idade)
a1.falar()
a1.estudar()
