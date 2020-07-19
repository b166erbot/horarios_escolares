from typing import List, Callable


def pegar_entradas_loop(
    funcao_aquisitora: Callable, itens: List[str]
) -> List[str]:
    """Pega entradas do usuário até o mesmo digitar não."""

    textos = []
    nova_entrada = 's'
    while nova_entrada and nova_entrada in 'sy':
        entrada = funcao_aquisitora(itens)
        nova_entrada = input('continuar? [s/n]: ').lower()
        textos.append(entrada)
        print()
    return textos


def pegar_entradas(itens):
    """Pega as entradas do usuário e retorna como uma lista."""
    lista = []
    for item in itens:
        lista.append(input(f"{item}> ").lower())
    return lista
