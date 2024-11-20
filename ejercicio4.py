def convertirMedida(cantidad:float, unidad1:str, unidad2:str)-> float:
    if unidad1 == "gramos" and unidad2 == "kilos":
        cantidadConvertida = cantidad / 1000
    elif unidad1 == "gramos" and unidad2 == "toneladas":
        cantidadConvertida = cantidad / 1000000
    elif unidad1 == "kilos" and unidad2 == "gramos":
        cantidadConvertida = cantidad * 1000
    elif unidad1 == "kilos" and unidad2 == "toneladas":
        cantidadConvertida = cantidad / 1000
    elif unidad1 == "toneladas" and unidad2 == "gramos":
        cantidadConvertida = cantidad * 1000000
    elif unidad1 == "toneladas" and unidad2 == "kilos":
        cantidadConvertida = cantidad * 1000
    elif unidad1 == unidad2:
        cantidadConvertida = cantidad
    else:
        print("opcion invalida")
    return cantidadConvertida

cantidad = float(input("Introduce una cantidad: "))
unidad1 = str(input("Introduce unidad origen (gramos, kilos, toneladas): "))
unidad2 = str(input("Introduce unidad destino (gramos, kilos, toneladas): "))
resultado = convertirMedida(cantidad, unidad1, unidad2)
print(f"{cantidad} {unidad1} son {resultado} {unidad2}")
