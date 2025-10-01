month = int(input('Insira o número de um mês (1 a 12): '))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('Esse mês tem 31 dias')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('Esse mês tem 30 dias')
else:
    print('Esse mês tem 29 dias')
