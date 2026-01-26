"""
OBI 2018 - Modalidade Programação
Fase: 1
Nível: Sênior
Problema: Piso da escola
Autora: Camila Vergara
"""

L = int(input())
C = int(input())


l1 = L * C + (L-1) * (C-1)
l2 = (L-1) * 2 + (C-1) * 2

print(l1)
print(l2)