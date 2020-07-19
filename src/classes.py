from functools import namedtuple


semana_nomes = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')

# namedtuples não aceita inteiros como atributos
# horarios = namedtuple(
#     'horarios', ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
# )


# class Horarios:
#     def __init__(self):
#         self._primeiro = ''
#         self._segundo = ''
#         self._terceiro = ''
#         self._quarto = ''
#         self._quinto = ''
#
#     def __iter__(self):
#         return iter(self.tudo)
#
#     @property
#     def tudo(self):
#         return [
#             self._primeiro, self._segundo, self._terceiro, self._quarto,
#             self._quinto
#         ]
#
#     def atribuir(self, ProfessorMateria, horario):
#         getattr(self, '_' + horario) = ProfessorMateria


# class Semana:
#     def __init__(self):
#         self._segunda = Horarios()
#         self._terca = Horarios()
#         self._quarta = Horarios()
#         self._quinta = Horarios()
#         self._sexta = Horarios()
#
#     @property
#     def tudo(self):
#         return [
#             self._segunda, self._terca, self._quarta, self._quinta, self._sexta
#         ]



# class Horario:
#     def __init__(self, professor, materia, horario, fixo):
#         self._professor = professor
#         self._materia = materia
#         self._horario = horario
#         self._fixo = fixo
#
#     def __repr__(self):
#         return f"{self._horario}: {self._professor} - {self._materia}"


class ProfessorMateria:
    def __init__(self, professor, materia):
        self._professor = professor
        self._materia = materia

    def __repr__(self):
        return f"{self._professor}: {self._materia}"


class HorarioVazio:
    _professor = 'vazio'
    def __repr__(self):
        return "Horário vazio"
