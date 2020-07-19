from texttable import Texttable
from typing import NoReturn
from collections import namedtuple
from random import shuffle, choice

from .entradas import pegar_entradas, pegar_entradas_loop
from .classes import (
    semana_nomes, ProfessorMateria, HorarioVazio
)
# remover horários? ^
from .ferramentas import cortar, completar, alternar


# renomear o minhas ferramentas e mandar pro git como repo privado.
# zip(random.shuffle(listas))
def main() -> NoReturn:
    print(
        '\ndigite o nome do professor[texto], sua matéria[texto] e o '
        'número[número] de vezes que o professor precisa dar a matéria'
        ' durante a semana.\n'
    )
    entradas = pegar_entradas_loop(
        pegar_entradas, ('nome', 'matéria', 'vezes')
    )
    materias = [
        ProfessorMateria(professor, materia)
        for (professor, materia, vezes) in entradas
        for _ in range(int(vezes))
    ]
    # completar com espaços vazios
    if len(materias) < 25:
        materias += completar(materias, 25, HorarioVazio)
    misturar = 's'
    alternar = input('alternar professor uma vez por dia? [s/n]: ')
    while misturar == 's':
        tabela = Texttable()
        shuffle(materias)
        materias_ = cortar(materias, 5)
        if alternar == 's':
            materias_ = alternar(materias)
        tabela.add_rows(
            (semana_nomes, *zip(*materias_))
        )
        print(tabela.draw())
        misturar = input('deseja misturar novamente? [s/n]: ')
