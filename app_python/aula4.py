# a = int(input('Entre com o número: '))

# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1

# if div == 2:
#     print('Número {} é primo!' .format(a))
# else:
#     print('Número {} não é primo!' .format(a))


# a = int(input('Entre com um número para descobrir quais são os números primos até ele: '))
# for numero in range(a+1):
#     div = 0
#     for x in range(1, numero + 1):
#         resto = numero % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1

#     if div == 2:
#         print(numero)


# a = 0
# while a <= 10:
#     print(a)
#     a += 1


# nota = int(input('Entre com a nota do : '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta:'))


a = int(input('Nota Primerio bimestre: '))
while a > 10:
    a = int(input('Você digitou algo errado. Nota Primeiro bimestre:'))
b = int(input('Nota Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou algo errado. Nota Segundo bimestre:'))
c = int(input('Nota Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou algo errado. Nota Terceiro bimestre:'))
d = int(input('Nota Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou algo errado. Nota Quarto bimestre:'))
media = (a + b + c + d) / 4
print('Sua média anual é: {}' .format(media))
