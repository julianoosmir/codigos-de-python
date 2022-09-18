from enum import Enum

class Meses(Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARÇO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6
    JULHO = 7
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12

def imprimirDataDeNascimento(dia, mes,ano):
    print(dia, 'de', Meses(mes).name,'de', ano)

print('digite sua data')
dia = int(input('dia :'))
mes = int(input('mes :'))
ano = input('ano :')

imprimirDataDeNascimento(dia,mes,ano)

