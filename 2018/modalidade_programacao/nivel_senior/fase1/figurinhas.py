"""
OBI 2018 - Modalidade Programação
Fase: 1
Nível: Sênior
Problema: Figurinhas da Copa
Autora: Camila Vergara
"""

N, C, M = [int(i) for i in input().split()]

carimbadas = [int(i) for i in input().split()]
compradas = [int(i) for i in input().split()]

contador = C
for x in carimbadas:
    if x in compradas:
        contador -= 1
        
print(contador)

