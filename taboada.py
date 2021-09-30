contador = 0
x = int(input('Qual numero deseja fazer a taboada? '))
while contador <= 10:
    resultado = x * contador
    print(x,'x',contador,'=',resultado)
    contador += 1
