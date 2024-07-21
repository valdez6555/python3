def convertir_pesos_a_dolares(cantidad_en_pesos):
    tasa_de_cambio = 18  # 1 USD = 18 MXN
    cantidad_en_dolares = cantidad_en_pesos / tasa_de_cambio
    return cantidad_en_dolares

def main():
    try:
        cantidad_pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
        cantidad_dolares = convertir_pesos_a_dolares(cantidad_pesos)
        print(f"{cantidad_pesos:.2f} MXN equivale a {cantidad_dolares:.2f} USD")
    except ValueError:
        print("Ingresa una cantidad válida en pesos mexicanos.")

if __name__ == "__main__":
    main()

