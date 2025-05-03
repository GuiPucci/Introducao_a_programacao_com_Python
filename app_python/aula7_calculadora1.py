class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


calculadora = Calculadora(10, 2)
print("Valor 1 =", calculadora.valor_a)
print("Valor 2 =", calculadora.valor_b)
print("Soma:", calculadora.soma())
print("Subtração:", calculadora.subtracao())
print("Divisão:", calculadora.divisao())
print("Multiplicação:", calculadora.multiplicacao())
