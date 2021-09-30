n = int(input('Quantos numeros quer testar? '))
numeros = []
contador = 1
while contador <= n:
    numeros.append(int(input('Digite o numero: ')))
    contador += 1
print(max(numeros))
print(min(numeros))
print(sum(numeros)/n)