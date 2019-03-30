def suma(a, b):
    suma = a + b
    return suma


def resta(a, c):
    resta = a - b
    return resta


def producto(a, b):
    producto = a * b
    return producto


def division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    else:
        return division


def potencia(a, b):
    potencia = a ** b
    return potencia
