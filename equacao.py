def raizes(a, b, c):
    delta = b ** 2  - 4 * a * c
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    return x1, x2

#Programa

a = input("Digite o valor de a: ")
a = int(a)
b = input("Digite o valor de b: ")
b = int(b)
c = input("Digite o valor de c: ")
c = int(c)

raizes = raizes(a, b, c)
print(f"As raízes da equação são: {raizes}")

