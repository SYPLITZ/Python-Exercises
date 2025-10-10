def confi_triangulos(a, b, c):
    if a + b > c and c + a > b and b + c > a:
        triangulo_confirmacao = 'positivo'
    else:
        triangulo_confirmacao = 'negativo'
        return triangulo_confirmacao
def qual_triangulo(triangulo_confirmacao):
    if triangulo_confirmacao == 'positivo':
        if b == c != a and a == c != b and a == b != c:
            tipo_triangulo = 'isosceles'
        elif b == a == c:
            tipo_triangulo = 'equilatero'
        elif b != a != c:
            tipo_triangulo = 'escaleno'
            return tipo_triangulo
def retangulo(a, b, c):
    teorema = (a**2) + (b**2) 
    if teorema == c ** 2
        retangulo_confirmacao = 'positivo'
    else:
        retangulo_confirmacao = 'negativo'
        return retangulo_confirmacao

# programa

#catetos e hipotenusa
c = int(input('Digite a hipotenusa: '))
b = int(input('Digite o primeiro cateto: '))
a = int(input('Digite o segundo cateto: '))
#variaveis funções
triangulo_confirmacao = confi_triangulos(a, b, c)
tipo_triangulo = qual_triangulo(triangulo_confirmacao)
retangulo_confirmacao = retangulo(a, b, c):
#execução final
    if triangulo_confirmacao == 'positivo':
        print(f'O seu triangulo é um triangulo {tipo_triangulo}')
        if retangulo_confirmacao == 'positivo':
            print('Esse triângulo é retângulo!')
        else:
            if retangulo_confirmacao == 'negativo':
                print('Não é retângulo')

    else:
        if triangulo_confirmacao == 'negativo':
            print('Não é possível de se formar um triângulo...')
            
