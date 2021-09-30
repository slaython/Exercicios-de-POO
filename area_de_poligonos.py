print('Área de POLIGONOS')
dnv = 's'
while dnv == 's':
    lados = int(input('Quatos lados tem o poligono? '))
    if lados == 3:
        base = float(input('Qual a base? '))
        altura = float(input('Qual a altura? '))
        area = (base * altura)/2
        print('O poligono é um TRIÂNGULO com area =',area,'.')
    elif lados == 4:
        base = float(input('Qual a base? '))
        altura = float(input('Qual a altura? '))
        area = base * altura
        print('O poligono é um QUADRADO com area =', area, '.')
    elif lados == 5:
        print('O poligono é um PENTAGONO.')
    else:
        print('Poligono não cadastrado.')
    dnv = input('\nQuer testar outro poligono ? s-sim: ')
print('Obrigado, até mais :)')