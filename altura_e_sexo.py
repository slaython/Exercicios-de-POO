print('Calculo de peso idael!')
sexo = input('Qual seu sexo? F-feminino ou M-masculino: ')
altura = float(input('Qual sua altura? exemplo(1.57)cm: '))
if sexo == 'F' and altura < 1.55:
    print('Seu peso ideal fica entre 49kg a 52kg.')
elif sexo == 'F' and altura >= 1.55 and altura < 1.60:
    print('Seu peso ideal fica entre 53kg a 56kg.')
elif sexo == 'F' and altura >= 1.60 and altura < 1.70:
    print('Seu peso ideal fica entre 55kg a 63kg.')
elif sexo == 'F' and altura >= 1.70 and altura < 1.80:
    print('Seu peso ideal fica entre 64kg a 70kg.')
elif sexo == 'F' and altura >= 1.80 and altura < 1.85:
    print('Seu peso ideal fica entre 71kg a 74kg.')
elif sexo == 'M' and altura < 1.60:
    print('Seu peso ideal fica entre 54kg a 57kg.')
elif sexo == 'M' and altura >= 1.60 and altura < 1.70:
    print('Seu peso ideal fica entre 58kg a 64kg.')
elif sexo == 'M' and altura >= 1.70 and altura < 1.80:
    print('Seu peso ideal fica entre 65kg a 71kg.')
elif sexo == 'M' and altura >= 1.80 and altura < 1.90:
    print('Seu peso ideal fica entre 72kg a 79kg.')
else:
    print('Dados não cadastrados.')