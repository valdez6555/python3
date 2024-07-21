def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

# Pedimos al usuario que ingrese los números y la operación
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")

# Realizamos la operación correspondiente
if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    resultado = division(num1, num2)
else:
    resultado = "Operación no válida"

# Mostramos el resultado
print(f"El resultado de la operación es: {resultado}")
