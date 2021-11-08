lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotacao = 5
contagem = 0

while contagem < rotacao:
    lista.insert(0, lista[-1])
    lista.pop(-1)
    contagem += 1
print(lista)
