class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


if __name__ == "__main__":
    calculadora = Calculadora()
    print("Soma:", calculadora.soma(10, 2))
    print("Subtração:", calculadora.subtracao(5, 3))
    print("Divisão:", calculadora.divisao(100, 2))
    print("Multiplicação:", calculadora.multiplicacao(10, 5))
