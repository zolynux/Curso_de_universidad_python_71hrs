"""Decoradores
Un decorador es una función que recibe una función y regresa otra
lo utilizamos para extender funcionalidad
1. Función decorador (a)
2. Función a decorar (b)
3. Función decorada (c)
"""


# * Se para como parámetro al decorador de manera automática
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print("Antes de ejecutar la función")
        funcion_a_decorar_b()
        print("Después de ejecutar la función")

    return funcion_decorada_c


@funcion_decorador_a
def mostrar_mensaje():
    print("Hola desde función mostrar_mensaje")


mostrar_mensaje()

print()


@funcion_decorador_a
def imprimir():
    print("Hola desde función imprimir")


imprimir()
