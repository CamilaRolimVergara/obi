"""
OBI 2020 - Modalidade Programação
Fase: 1 - Turno A
Nível: Sênior
Problema: Acelerador de partículas
Autora: Camila Vergara
"""

D = int(input())

saida = (D - 3)%8

if saida == 3:
    print(1)
elif saida == 4:
    print(2)
else:
    print(3)


