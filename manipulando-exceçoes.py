"""def algo():
    raise Exception("Exceção!!")
    print("Depois da exceção!!")


def algo2():
    try:
        algo()
    except:
        print("Eu peguei uma exceção!!")
        print("Executado após a exceção!!")


algo2()"""


"""def divisao(divisor):

    try:
        if divisor == 17:
            raise ValueError("Não poderá digitar o valor 17")
        return 10/divisor
    except ZeroDivisionError:
        return "Entre com um número diferente de zero!"
    except TypeError:
        return "Entre com um valor numérico!"
    except ValueError:
        print("Não utilize o valor 17!")
        raise


print(divisao(17))"""

try:
    raise ValueError("Este é um argumento!!")
except ValueError as e:
    print(f"Os argumentos da exceção foram {e}")
finally:
    print("Isso sempre será executado!!")