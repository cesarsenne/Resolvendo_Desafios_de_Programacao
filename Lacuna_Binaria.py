print('-=' * 30)
print('Lacuna Binaria'.center(60))
print('Converta um número para binário'.center(60))
print('E descubra quais são suas lacunas binarias'.center(60))
print('-=' * 30)
numero = int(input("Digite um número: "))
print('-=' * 30)
binario = "{0:b}".format(numero)

contagem_0 = 0
contagem_1 = 0
lista = []

for i in binario:
    if i == "1":
        contagem_1 += 1
        if contagem_1 == 2:
            contagem_1 = 1
            if contagem_0 != 0:
                lista.append(int(contagem_0))
                contagem_0 = 0
    elif i == "0":
        contagem_0 += 1
if not lista:
    lista.append(int(0))

maximo = max(lista)
minimo = min(lista)

print(f"O número \033[1m{numero}\033[0m convertido em binário é: \033[1m{binario}\033[0m")
print(f"Ao todo foram encontradas as seguintes lacunas binarias:\033[1m{lista}\033[0m")
print(f"A maior lacuna binaria foi de: \033[1m{maximo}\033[0m zeros")
print(f"A menor lacuna binaria foi de: \033[1m{minimo}\033[0m zeros")
print('-=' * 30)
