def contarPalabras():
    contador = 0

    while True:
        palabra = input("Introduce una palabra (escribe fin para terminar): ")
        if palabra == "fin":
            break
        if len(palabra) <= 5:
            contador += 1

    print(f"Has introducido {contador} palabras de 5 o menos letras.")

contarPalabras()
