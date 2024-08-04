from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    # Método isinstance y polimorfismo
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Juan", 5000)
imprimir_detalles(empleado)

gerente = Gerente("Karla", 6000, "Sistemas")
imprimir_detalles(gerente)
