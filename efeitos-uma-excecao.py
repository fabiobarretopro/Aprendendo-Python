def algo():
    print("Antes da chamada da função!")
    algo2()
    print("Depois da chamada da função!")


def algo2():
    raise Exception("Exceção em algo2()")

algo()