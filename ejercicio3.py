diaSemana = input("Introduce el día de la semana: ")
tipoHabitacion = input("Introduce el tipo de habitacion (individual o doble): ")
festivo = input("¿Es un día festivo? (Si o no): ")
tieneCupon = input("¿Tienes un cupón? (Si o no): ")

if festivo == "si" or diaSemana== "viernes" or diaSemana == "sabado":
    if tipoHabitacion == "individual":
        precio = 45
    elif tipoHabitacion == "doble":
        precio = 70
elif diaSemana == "domingo":
    if tipoHabitacion == "individual":
        precio = 40
    elif tipoHabitacion == "doble":
        precio = 60
else:
    if tipoHabitacion == "individual":
        precio = 30
    elif tipoHabitacion == "doble":
        precio = 50

if tieneCupon == "si":
    descuento = int(input("Introduce el descuento del cupon (0-100): "))
    precio -= precio * (descuento / 100)

print(f"El precio final de la habitación es: {precio}€")
