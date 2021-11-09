inicio = 0
primeiro = 0
segundo = 1
contador = 0

numero = int(input('Quantos números da sequência fibonacci você quer mostrar: '))

print('{} → {}'.format(primeiro, segundo), end=' → ')

while contador <= numero:
    inicio = primeiro + segundo
    primeiro = segundo
    segundo = inicio
    contador = contador + 1
    print('{}'.format(inicio), end=' → ')

print('Fim')
