def cortar(lista, numero):
    return [lista[x: x + numero] for x in range(0, len(lista), numero)]


def completar(lista, tamanho, item):
    faltando = tamanho - len(lista)
    return [item() for _ in range(faltando)]


def alternar(materias_cortadas):
    materias = list(map(
        lambda lista: sorted(
            lista, reverse=choice((True, False))),
            key = lambda ProfessorMateria: ProfessorMateria._professor
        ),
        materias_cortadas
    ))
    return materias
