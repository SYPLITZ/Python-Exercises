person_1 = input('Insira o nome da primeira pessoa: ')
age_1 = int(input('Insira a idade dessa pessoa: '))
person_2 = input('Insira o nome da segunda pessoa: ')
age_2 = int(input('Insira a idade da segunda pessoa: '))

if age_1 > age_2:
    print(f'O(a) {person_1} é mais velho!')
elif age_2 > age_1:
    print(f'O(a) {person_2} é o mais velho!')
else:
    print('Ambos possuem a mesma idade!')