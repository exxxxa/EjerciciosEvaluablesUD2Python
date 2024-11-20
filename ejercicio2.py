import random

pares = 0
impares = 0

for i in range(10):
    numero = random.randint(20,40)
    print(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1

porcentajePares = (pares/10) * 100
porcentajeImpares = (impares/10) * 100

print(f"Porcentaje de números pares: {porcentajePares}%")
print(f"Porcentaje de números impares: {porcentajeImpares}%")