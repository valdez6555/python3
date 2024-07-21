def calcular_imc():
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        imc = peso / (altura ** 2)

        print(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Tienes bajo peso.")
        elif 18.5 <= imc < 25:
            print("Tu peso está dentro del rango normal.")
        elif 25 <= imc < 30:
            print("Tienes sobrepeso.")
        else:
            print("Tienes obesidad.")

    except ValueError:
        print("Ingresa valores numéricos válidos para peso y altura.")

if __name__ == "__main__":
    calcular_imc()
