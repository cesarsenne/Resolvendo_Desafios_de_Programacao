from random import randint

matriz = []
elementos_ausentes = []
tamanho_da_matriz = 5

while len(matriz) < tamanho_da_matriz:
    sorteio = randint(0, tamanho_da_matriz)
    if sorteio not in matriz:
        matriz.append(sorteio)
print(matriz)

maximo = max(matriz)
contador = 0
while contador <= tamanho_da_matriz:
    for item in matriz:
        if contador not in matriz:
            if contador not in elementos_ausentes:
                elementos_ausentes.append(contador)
    contador += 1
print(elementos_ausentes)
