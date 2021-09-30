joao = 0
maria = 0
jose = 0
severina = 0
nulo = 0
branco = 0
contador = 1
x = int(input('Quantas pessoas irão votar? '))
print('VOTAÇÃO - Escolha o código e vote:')
print('1 - JOAO')
print('2 - MARIA')
print('3 - JOSE')
print('4 - SEVERINA')
print('5 - NULO')
print('6 - EM BRANCO')
while contador <= x:
    voto = int(input('Qual seu voto? '))
    if voto == 1:
        joao = joao + 1
    elif voto == 2:
        maria = maria + 1
    elif voto == 3:
        jose = jose + 1
    elif voto == 4:
        severina = severina + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    else:
        print('Voto não cadastrado!')
    contador += 1
print('O total de votos para cada candidato foi:\nJOAO=',joao,'\nMARIA=',maria,'\nJOSE=',jose,'\nSEVERINA=',severina)
print('NULOS=',nulo,'\nEM BRANCO=',branco)
perc_nulos = (nulo/x)*100
perc_branco = (branco/x)*100
print('O percentual de nulos foi de',perc_nulos,'%')
print('O percentual de votos em branco foi de',perc_branco,'%')