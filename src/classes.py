from functools import namedtuple
from random import shuffle
from itertools import chain

semana_nomes = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')


class Semana:
    def __init__(self):
        self._semana = {
            'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [],
            '': []
        }
        self._horarios = {
            'segunda3:00': 0, 'segunda3:30': 1, 'segunda4:00': 2,
            'segunda4:30': 3, 'segunda5:00': 4, 'terça3:00': 5, 'terça3:30': 6,
            'terça4:00': 7, 'terça4:30': 8, 'terça5:00': 9, 'quarta3:00': 10,
            'quarta3:30': 11, 'quarta4:00': 12, 'quarta4:30': 13,
            'quarta5:00': 14, 'quinta3:00': 15, 'quinta3:30': 16,
            'quinta4:00': 17, 'quinta4:30': 18, 'quinta5:00': 19,
            'sexta3:00': 20, 'sexta3:30': 21, 'sexta4:00': 22, 'sexta4:30': 23,
            'sexta5:00': 24
        }

    def tudo(self):
        # return list(chain(*self._semana.values()))
        horarios = self._semana[''][:]
        semana = chain(*list(self._semana.values())[:-1])
        semana = sorted(
            semana, key=lambda x: self._horarios.get(x.semana_hora(), 25)
        )
        for horario in semana:
            semana_hora = horario.semana_hora()
            if semana_hora in self._horarios:
                horarios.insert(self._horarios[semana_hora], horario)
            else:
                horarios.append(horario)
        return horarios


    def sacudir(self):
        shuffle(self._semana[''])

    def adicionar(self, dia_semana, horario):
        self._semana[dia_semana].append(horario)

    def __len__(self):
        return sum(map(len, self._semana.values()))


class Horario:
    def __init__(self, professor, materia, horario, semana):
        self._professor = professor
        self._materia = materia
        self._horario = horario
        self._semana = semana

    def __repr__(self):
        return f"{self._horario} - {self._professor} - {self._materia}"

    def semana_hora(self):
        return self._semana + self._horario


class HorarioVazio:
    _professor = 'vazio'
    def __repr__(self):
        return "Horário vazio"
