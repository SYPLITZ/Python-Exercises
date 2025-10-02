#Valor em binário, decimal e operador
binary_number_1 = input('Primeiro número em binário: ')
binary_number_2 = input('Segundo número em binário: ')
operator = input('Insira um operador: ')
value1 = int(binary_number_1, 2)
value2 = int(binary_number_2, 2)
#Operação com Soma
if operator == '+':
 result = value1 + value2
 print(f'O valor da soma em binário é igual: {bin(result)}')
 print(f'O valor da soma em octal é igual: {oct(result)}')
 print(f'O valor da soma em inteiro é igual: {int(result)}')
 print(f'O valor da soma em hexadecimal é igual: {hex(result)}')
 #Operação com Subtração
elif operator == '-':
 result = value1 - value2
 print(f'O valor em binário da subtração é igual a: {bin(result)}')
 print(f'O valor em octal da subtração é: {oct(result)}')
 print(f'O valor em inteiro da subtração é: {int(result)}')
 print(f'O valor em hexadecimal da subtração é: {hex(result)}') 
#Operações de Multiplicação
elif operator == '*':
 result = value1 * value2
 print(f'O valor em binário da subtração é: {bin(result)}')
 print(f'O valor em octal da subtração é: {oct(result)}')
 print(f'O valor em inteiro da subtração é: {int(result)}')
 print(f'O valor em hexadecimal da subtração é: {hex(result)}')
 #Operações de Divisão
elif operator == '/':
 if value2 != 0:
    result = value1 // value2
    print(f'O valor em binário: {bin(result)}')
    print(f'O valor em octal: {oct(result)}')
    print(f'O valor por inteiro é: {int(result)}')
    print(f'O valor em hexadecimal é igual a: {hex(result)}')
#Quando é por zero
 else:
   print('nao é permitida a divisao por zero')





