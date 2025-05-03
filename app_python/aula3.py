
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))

# if a > b:
#     print('O maior número é: {}'.format(a))
# else:
#     print('O maior número é: {}' .format(b))
# print('Final do programa.')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('O maior número é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é: {}' .format(b))
# else:
#     print('O maior número é: {}' .format(c))
# print('Final do programa.')


# a = int(input('Entre com um valor: '))
# resto = a % 2

# if resto == 0:
#     print('O número é PAR')
# else:
#     print('O número é IMPAR')


# a = int(input('Entre com o primero valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2

# if resto_a == 0 or not resto_b != 0:
#     print('Foi digitado um número par.')
# else:
#     print('Nenhum número par foi digitado.')


# a = int(input('Nota Primerio bimestre: '))
# b = int(input('Nota Segundo bimestre: '))
# c = int(input('Nota Terceiro bimestre: '))
# d = int(input('Nota Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Sua média anual é: {}' .format(media))
# else:
#     print('Foi informada alguma nota errada!')


a = int(input('Nota Primerio bimestre: '))
if a > 10:
    a = int(input('Você digitou algo errado. Nota Primeiro bimestre:'))
b = int(input('Nota Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou algo errado. Nota Segundo bimestre:'))
c = int(input('Nota Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou algo errado. Nota Terceiro bimestre:'))
d = int(input('Nota Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou algo errado. Nota Quarto bimestre:'))
media = (a + b + c + d) / 4
print('Sua média anual é: {}' .format(media))
