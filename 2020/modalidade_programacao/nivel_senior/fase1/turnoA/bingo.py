"""
OBI 2020 - Modalidade Programação
Fase: 1 - Turno A
Nível: Sênior
Problema: Bingo!
Autora: Camila Vergara
"""

N, K, U = [int(x) for x in input().split()]

cartelas = [set() for _ in range(N)]

for i in range(N):
    cartelas[i] = set(int(x) for x in input().split())

numeros_sorteados = [int(x) for x in input().split() for _ in range(U)]

cartelas_vencedoras = []
for numero in numeros_sorteados:
        for i in range(N):
            if numero in cartelas[i]:
                cartelas[i].remove(numero)
                if len(cartelas[i]) == 0:
                    cartelas_vencedoras.append(i + 1)
        if cartelas_vencedoras != []:
            break 

print(*cartelas_vencedoras)