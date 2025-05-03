# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

def contador_letras(lista): return [len(x) for x in lista]


lista_animais = ["cachorro", "gato", "elefante"]
print(contador_letras(lista_animais))

# fmt: off
soma = lambda a, b: a + b 
subtracao = lambda a, b: a - b  
# fmt: on

print(soma(5, 10))
print(subtracao(10, 5))


calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora["soma"]
# soma: lambda a, b: a + b,
subtracao = calculadora["subtracao"]
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["divisao"]
print(f"A soma é:", soma(10, 5))
print(f"A multiplicação é: {multiplicacao(10, 2)}")
