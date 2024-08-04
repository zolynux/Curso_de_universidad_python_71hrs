# Unpacking en Python

# Parte - 1
print("Parte-1".center(60, "-"))

valores = 1, 2, 3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

# Variable a omitir en valor 2
valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)


valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)
print(f"valor3: {type(valor3)}")

# Parte - 2
print("Parte-2".center(60, "-"))

valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(f"valor3: {type(valor3)}")


def regresa_varios_datos():
    return 1, 2, 3


valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

print("Ejemplo de Unpacking".center(60, "-"))

# help(str.partition)

hora, separador, minutos = "17:20".partition(":")
# print(type(variable))
print(hora, separador, minutos)

hora, _, minutos = "17:20".partition(":")
print(hora, minutos)
