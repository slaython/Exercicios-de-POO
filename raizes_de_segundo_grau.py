dnv = 's'
while dnv == 's':
    print('ax² + bx + c = 0')
    a = int(input('Qual valor da variavel a? '))
    b = int(input('Qual valor da variavel b? '))
    c = int(input('Qual valor da variavel c? '))
    delta = (b ** 2) - (4 * a * c)
    x1 = ( (-b) + (delta ** (1/2) ) )/ (2 * a)
    x2 = ( (-b) - (delta ** (1/2) ) )/ (2 * a)
    print(x1,x2)
    dnv = input('Quer testar novamente? s-sim: ')
print('Obrigado, até mais :)')