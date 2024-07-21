def clasificar_edad(edad):
    if edad < 0:
        return "Edad inválida (debe ser un número positivo)"
    elif edad < 18:
        return "Eres adolecente."
    else:
        return "Eres mayor de edad."

# Solicita la entrada del usuario
try:
    edad_usuario = int(input("Ingresa tu edad: "))
    resultado = clasificar_edad(edad_usuario)
    print(resultado)
except ValueError:
    print("Ingresa un número válido para la edad.")
