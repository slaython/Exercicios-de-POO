celsius = 0
fahrenheit = 0
kelvin = 0
dnv = 's'
print('Conversor de temperatura, escolha qual unidade quer converter:')
while dnv == 's':
    print('1 - Celsius\n2 - Farenheit\n3 - Kelvin')
    escolha = int(input('Qual unidade voce quer converter? '))
    if escolha == 1:
        temperatura = float(input('Qual a temperatura quer converter? '))
        kelvin = temperatura + 273
        fahrenheit = temperatura * 1.8 + 32
        print(temperatura,'°C é igual a',kelvin,'°K e',fahrenheit,'°F.')
    elif escolha == 2:
        temperatura = float(input('Qual a temperatura quer converter? '))
        celsius = (temperatura - 32)/1.8
        kelvin = (temperatura -32)* (5/9)+ 273
        print(temperatura,'°F é igual a',celsius,'°C e',kelvin,'°K.')
    elif escolha == 3:
        temperatura = float(input('Qual a temperatura quer converter? '))
        celsius = temperatura - 273
        fahrenheit = (temperatura-273)*1.8+32
        print(temperatura,'°K é igual a',celsius,'°C e',fahrenheit,'°F.')
    else:
        print('Escolha não cadastrada!')
    dnv = input('Quer converter novamente? ')
print('Até mais. :)')