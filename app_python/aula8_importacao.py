from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from Aula8_contador_letras import contador_letras, teste


if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ["cachorro", "gato", "elefante"]
    total_letras = contador_letras(lista)
    print(f"Total de letras por palvras da lista:, {total_letras}")
    print(teste())
