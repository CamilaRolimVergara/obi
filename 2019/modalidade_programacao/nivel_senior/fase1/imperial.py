"""
OBI 2019 - Modalidade Programação
Fase: 1
Nível: Sênior
Problema: Calçada Imperial
Autora: Camila Vergara
"""

n = int(input())
seq = [int(input()) for _ in range(n)]

dp = {}     
seen = set()
resposta = 1

for x in seq:
    for y in list(seen):
        if y != x:
            valor = dp.get((x, y), 1) + 1
            dp[(y, x)] = max(dp.get((y, x), 0), valor)
            resposta = max(resposta, dp[(y, x)])
        
    seen.add(x)

print(resposta)