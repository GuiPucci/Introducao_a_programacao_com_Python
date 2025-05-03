# a = 10
# b = 5
# soma = a + b
# subtracao = a - b
# multiplicacao = a * b
# divisao = a / b
# resto = a % b


# print(multiplicacao)
# print(divisao)
# print(type(divisao))
# print(int(divisao))
# print(type(soma))
# print(type(subtracao))
# print('soma: ' + str(soma))
# print('subtracao: ' + str(subtracao))
# print(resto)


# x = "1"
# soma2 = int(x) + 1
# print(soma2)

# print('soma: {}. subtração: {}' .format(soma, subtracao))

# print('soma: {soma}. subtração: {subtracao}' .format(
#     soma=soma, subtracao=subtracao))

# print('soma: {soma}. \nsubtração: {subtracao}' .format(
#     soma=soma, subtracao=subtracao))

a = int(input('Entre com o primerio valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}. \nSubtração: {subtracao}.'
             '\nMultiplicacação: {multiplicacao}.'
             '\nDivisão: {divisao}. '
             '\nResto: {resto}' .format(soma=soma, subtracao=subtracao,
                                        multiplicacao=multiplicacao, divisao=divisao, resto=resto))
print(resultado)
