#Função de Confirmar se é Triângulo
def confi_triangulos(a, b, c):
    if a + b > c and c + a > b and b + c > a:
        return 'positivo'
    else:
        return 'negativo'
#Função para ver qual é o tipo do Triângulo    
def qual_triangulo(triangulo_confirmacao, a, b, c):
    if triangulo_confirmacao == 'positivo':
        if a == b and b == c:
            tipo_triangulo = 'equilatero'
        elif a == b or b == c or a == c:
            tipo_triangulo = 'isosceles'
        else:
            tipo_triangulo = 'escaleno'
    else:
        tipo_triangulo = None
    return tipo_triangulo
#Triângulo é Retângulo ou não?
def retangulo(a, b, c):
    if c**2 == a**2 + b**2:
        return 'positivo'
    else:
        return 'negativo'

#Entrada de Dados
a = int(input('Digite o valor do primeiro cateto: '))
b = int(input('Digite o valor do segundo cateto: '))
c = int(input('Digite o valor da hipotenusa: '))

#Variaveis Recebem Funções
triangulo_confirmacao = confi_triangulos(a, b, c)
tipo_triangulo = qual_triangulo(triangulo_confirmacao, a, b, c)
retangulo_confirmacao = retangulo(a, b, c)

#Execução Final
if triangulo_confirmacao == 'positivo':
    print(f'O seu triângulo é um triângulo {tipo_triangulo}!')
    if retangulo_confirmacao == 'positivo':
        print('Esse triângulo é retângulo!')
    else:
        print('Não é um triângulo retângulo...')
else:
    print('Não é possível formar um triângulo...')
