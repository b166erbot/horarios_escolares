from texttable import Texttable
from typing import NoReturn
from collections import namedtuple
from random import shuffle, choice

from .entradas import pegar_entradas, pegar_entradas_loop
from .classes import (
    semana_nomes, Horario, HorarioVazio, Semana
)
from .ferramentas import cortar, completar, alternar


def main() -> NoReturn:
    print(
        '\ndigite o nome do professor[texto], sua matéria[texto] e o '
        'número[número] de vezes que o professor precisa dar a matéria'
        ' durante a semana.\n'
    )
    entradas = pegar_entradas_loop(
        pegar_entradas, (
            'professor(a)', 'matéria', 'horario', 'semana'
        )
    )
    semana_ = Semana()
    for (professor, materia, horario, dia_semana) in entradas:
        semana_.adicionar(
            dia_semana, Horario(professor, materia, horario, dia_semana)
        )
    # completar com espaços vazios
    if len(semana_) < 25:
        horarios_ = completar(semana_.tudo(), 25, HorarioVazio)
        for horario_ in horarios_:
            semana_.adicionar('', horario_)
    misturar = 's'
    while misturar == 's':
        tabela = Texttable()
        semana_.sacudir()
        materias_ = cortar(semana_.tudo(), 5)
        tabela.add_rows(
            (semana_nomes, *zip(*materias_))
        )
        print(tabela.draw())
        misturar = input('deseja misturar novamente? [s/n]: ')
