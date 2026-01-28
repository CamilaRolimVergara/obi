"""
OBI 2020 - Modalidade Programação
Fase: 1 - Turno A
Nível: Sênior
Problema: Paciente zero
Autora: Camila Vergara
"""

N, C = map(int, input().split())

cadeias = {}
infectados = set()

for _ in range(C):
    dados = list(map(int, input().split()))
    
    P = dados[0]
    I = dados[1]
    
    lista = dados[2:2 + I]
    cadeias[P] = lista
    
    for x in lista:
        infectados.add(x)

pacientes_zero = []

for p in cadeias.keys():
    if p not in infectados:
        pacientes_zero.append(p)

pacientes_zero.sort()

for p in pacientes_zero:
    print(p)
