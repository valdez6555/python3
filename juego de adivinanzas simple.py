import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")

    while True:
        suposicion = int(input("Ingresa tu suposición: "))
        intentos += 1

        if suposicion == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif suposicion < numero_secreto:
            print("El número secreto es mayor. Sigue intentando.")
        else:
            print("El número secreto es menor. Sigue intentando.")

if __name__ == "__main__":
    jugar_adivinanza()
