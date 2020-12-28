"""lista = [0, 1, 2, 3, 4, 5]  # A lista é um objeto iterável!
lista = iter(lista)   # Transforma em iterador (Quando apresenta um objeto de cada vez)

print(next(lista))  # Esse método apresenta 1 por 1 item pq foi transformado em iterador.
print(next(lista))

print(hasattr(lista, "__iter__"))  # Para saber se é um objeto iterável!
print(hasattr(lista, "__next__"))  # Para saber se é um objeto iterador (Quando apresenta um objeto de cada vez)

# Se for um objeto iterável conseguimos exibir os objetos da lista pelo FOR
for v in lista:  # Porém quando executamos pelo FOR transformamos o objeto e iterador / porque
    print(v)     # exibe cada objeto em uma linha (Um de cada vez)."""

# import sys

# lista = list(range(1000))  # Recebe todos os valores de uma vez e salvando na memória. (NÃO É O IDEAL!!)
# print(sys.getsizeof(lista))  # Verificando quantos bytes de memória está usando no computador.

# GERADORES: Gera 1 valor de cada vez e não todos de uma vez para economizar na memória!!
import time


"""def gera():  # Ainda não é um gerador
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r"""


"""def gera():  # Isso  é um gerador, gera um elemento de cada vez, economizando memória.
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
for v in g:
    print(v)"""

# import time


"""def gera():  # Isso  é um gerador, gera um elemento de cada vez, economizando memória.
    variavel = "Valor 1"
    yield variavel
    variavel = "Valor 2"
    yield variavel
    variavel = "Valor 3"
    yield variavel


g = gera()
for v in g:
    print(v)
"""
import sys

"""lista = list(range(20))
for c in lista:
    print(c)"""
l1 = [x for x in range(100)]
print(type(l1))
print(sys.getsizeof(l1))
l2 = (x for x in range(100))  # Só o fato de ter posto entre parênteses se transformou em um GERADOR!!
print(type(l2))
print(sys.getsizeof(l2))


 # AS LISTAS VÃO RETER TODOS OS VALORES E SALVAR TODOS NA MEMÓRIA
 # OS GERADORES VÃO RETER, MAS NÃO VÃO SALVAR TODOS OS VALORES NA MEMÓRIA



