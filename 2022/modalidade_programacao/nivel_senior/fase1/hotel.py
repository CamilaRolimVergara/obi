"""
OBI 2022 - Modalidade Programação
Fase: 1 
Nível: Sênior
Problema: Hotel
Autora: Camila Vergara
"""

D = int(input())
A = int(input())
N = int(input())

C = N
if C > 15:
    C = 15

print((31 - N + 1)*(D + (C-1) * A))