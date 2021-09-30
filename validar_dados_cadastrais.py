dados = ['', 0, 0, '', '']
dados[0] = input('Qual o nome? ')
dados[1] = int(input('Qual a idade? '))
dados[2] = float(input('Qual o salario? '))
dados[3] = input('Qual o sexo? m-masculino ou f-feminino: ')
print("qual o estado civil?")
dados[4] = input('s-solteiro(a), c-casado(a), v-viuvo(a), d-divorciado(a): ')
if len(dados[0]) < 3:
    print('Nome tem que conter mais que 3 caracteres.')
    dados[0] = input('Digite o nome: ')
if dados[1] < 0 or dados[1] > 150:
    print('Idade inválida!')
    dados[1] = int(input('Digite a idade novamente: '))
if dados[2] < 0:
    print('Salario não pode ser menor que zero!')
    dados[2] = float(input('Digite o salario novamente: '))
if dados[3] != 'm' and dados[3] != 'f':
    print('Sexo nao cadastrado!')
    dados[3] = input('Digite o sexo novamente: ')
if dados[4] != 's' and dados[4] != 'c' and dados[4] != 'v' and dados[4] != 'd':
    print('Estado civil nao cadastrado!')
    dados[4] = input('Digite novamente o estado civil: ')
for dado in dados:
    print(dado)