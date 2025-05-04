
lista = [1, 10]

try:
    arquivo = open("notas.txt", "r")
    texto = arquivo.read
    divisao = 10 / 0
    numero = lista[3]
    print("Fecahando o arquivo")


except ZeroDivisionError:
    print("Não é possivel realizar divisao por 0")
except ArithmeticError:
    print("Houve um erro ao realizar uma operação aritimética")
except IndexError:
    print("Erro ao acessar um índice inválido da lista")
except Exception as ex:
    print(f"Erro desconhecido. Erro: {ex}")
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")
    print("Fecahando o arquivo")
    arquivo.close()
