from datetime import datetime

def calcular_edad():
    try:
        fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
        fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

        fecha_actual = datetime.now()
        edad = fecha_actual.year - fecha_nacimiento_dt.year

        # Ajustamos la edad si aún no se ha cumplido el día de nacimiento en el año actual
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento_dt.month, fecha_nacimiento_dt.day):
            edad -= 1

        # Calculamos los meses y días
        meses = (fecha_actual.month - fecha_nacimiento_dt.month) % 12
        dias = (fecha_actual - fecha_nacimiento_dt.replace(year=fecha_actual.year)).days

        print(f"Tienes {edad} años, {meses} meses y {dias} días de edad.")
    except ValueError:
        print("Formato de fecha incorrecto. Asegúrate de ingresar la fecha en el formato dd/mm/aaaa.")

if __name__ == "__main__":
    calcular_edad()
