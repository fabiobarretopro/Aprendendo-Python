notas_alunos = dict()


def notas(*num, sit=False):
    """

    :param num: As notas passadas para a função.
    :param sit: Se quer ou não quer mostrar a situação geral das notas.
    :return: Retorna o total de notas, o maior e menor valor, sua média e a situação geral das nota, caso for pedida.
    """
    notas_alunos["Total"] = len(num)
    notas_alunos["Maior"] = max(num)
    notas_alunos["Menor"] = min(num)
    notas_alunos["Média"] = sum(num)/len(num)
    if sit:
        if notas_alunos["Média"] >= 7:
            notas_alunos["Situação"] = "Boa"
        elif notas_alunos["Média"] < 5:
            notas_alunos["Situação"] = "Regular"
        else:
            notas_alunos["Situação"] = "Péssima"
    print(notas_alunos)


notas(5.8, 8.5, 6.5, 9.3, 7.4, sit=True)
help(notas)