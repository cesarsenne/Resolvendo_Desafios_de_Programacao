lista = [1, 2, 3, 4, 5, 1, 2, 3, 4]
impares = []

for item in lista:
    if item not in impares:
        impares.append(item)
    else:
        impares.remove(item)

print(impares)
