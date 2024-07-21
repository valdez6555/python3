def kg_a_libras(kilogramos):
    return kilogramos * 2.20462

# Ejemplo de uso
kilogramos = float(input("Ingresa la masa en kilogramos: "))
print(f"{kilogramos} kg equivale a {kg_a_libras(kilogramos):.2f} libras")
