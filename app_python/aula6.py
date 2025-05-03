# [] - Listas
# () - Tuplas
# {} - Conjuntos

# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)


# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print('Conjunto união: {}' .format(conjunto_uniao))
# conjunto_interseccao = conjunto.intersection(conjunto2)
# print('Conjunto intersecção {}' .format(conjunto_interseccao))
# conjunto_diferenca1 = conjunto.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto)
# print('Conjunto diferença 1 e 2: {}' .format(conjunto_diferenca1))
# print('Conjunto diferença 2 e 1: {}' .format(conjunto_diferenca2))
# conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
# print(f'Diferença simétrica: {conjunto_dif_simetrica}')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(f'A é um subconjunto de B: {conjunto_subset}')
print(f'A é um subconjunto de B: {"SIM" if conjunto_subset else "NÃO"}')
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(f'B é um subconjunto de A: {conjunto_subset}')
print(f'B é um subconjunto de A: {"SIM" if conjunto_subset else "NÃO"}')
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(f'B é um superconjunto de A: {"SIM" if conjunto_superset else "NÃO"}')
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print(f'A é um superconjunto de B: {"SIM" if conjunto_superset else "NÃO"}')


lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


# print('Conjunto diferença 2 e 1: {}' .format(conjunto_diferenca2))
# print('Conjunto diferença 2 e 1:', conjunto_diferenca2)
# print(f'Conjunto diferença 2 e 1: {conjunto_diferenca2}')
