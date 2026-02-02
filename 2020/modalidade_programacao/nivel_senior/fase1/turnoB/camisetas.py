"""
OBI 2020 - Modalidade Programação
Fase: 1 - Turno B
Nível: Sênior
Problema: Camisetas da Olimpíada
Autora: Camila Vergara
"""

N = int(input())

camisetas = [int(i) for i in input().split()]
p = camisetas.count(1)
m = camisetas.count(2)


P = int(input())
M = int(input())

if P >= p and M >= m:
    print('S')
else:           
    print('N')


