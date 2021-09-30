numero1 = 0
numero2 = 1
contador = 0
nivel = int(input('Qualo nivel do Fibonacci você quer testar ? '))
while contador <= nivel:
    if contador == 0:
        print(numero1)
    elif contador % 2 != 0:
        numero1 = numero2 + numero1
        print(numero1)
    elif contador % 2 == 0:
        numero2 = numero1 + numero2
        print(numero2)
    else:
        print('Errado')
    contador += 1