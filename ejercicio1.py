sumaTotal = 0
cantidadNumeros = 0
numMayor = 0
numMenor = 9999

while sumaTotal < 100:
    num = int(input("Introduce un número: "))

    sumaTotal += num
    cantidadNumeros += 1

    if num > numMayor:
            numMayor = num
    if num < numMenor:
        numMenor = num


media = sumaTotal / cantidadNumeros

print(f"Cantidad de números introducidos: {cantidadNumeros}")
print(f"Suma total: {sumaTotal}")
print(f"Media: {media}")
print(f"Número mayor: {numMayor}")
print(f"Número menor: {numMenor}")