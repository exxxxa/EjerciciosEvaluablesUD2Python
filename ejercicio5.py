def mostrarDivisores(numero:int):
    print(f"Los divisores de {numero} son:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

numero = int(input("Introduce un número entero: "))
mostrarDivisores(numero)
