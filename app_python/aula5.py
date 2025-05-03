# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
# print(lista)
# print(lista_animal[1])

# # soma = 0
# # for x in lista:
# #     print(x)
# #     soma += x
# # print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))

# print(max(lista_animal))
# print(min(lista_animal))

# if 'gato' in lista_animal:
#     print("Existe um gato na lista.")
# else:
#     print('Não existe um gato na lista.')


# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista.')
# else:
#     print('Não existe um lobo na lista.')


# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
# nova_lista = lista_animal * 3
# print(nova_lista)


# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']


# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista.')
# else:
#     print('Não existe um lobo na lista. Será incluído')
#     lista_animal.append("lobo")
#     print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

# lista = [12, 10, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)


lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[2])
# tupla[0] = 12 # Gera erro - Na tupla os valores sao imutaveis
print(len(tupla))  # len trs o comprimento, qunatidade
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)
