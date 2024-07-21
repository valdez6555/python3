def clasificar_edad(edad):
    if 1 <= edad <= 12:
        return "niño"
    elif 13 <= edad <= 18:
        return "adolescente"
    elif 19 <= edad <= 50:
        return "adulto"
    elif 50 < edad <= 100:
        return "anciano"
    else:
        return "Edad fuera del rango válido"

# Pide al usuario que ingrese su edad
try:
    edad_usuario = int(input("Ingresa tu edad: "))
    resultado = clasificar_edad(edad_usuario)
    print(f"Según la clasificación, tienes {resultado}.")
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")