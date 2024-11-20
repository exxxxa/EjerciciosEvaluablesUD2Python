def contarLetraPalabras(letra:str):
    contadorLetra = 0

    while True:
        palabra = input("Introduce una palabra (escribe fin para terminar): ")
        if palabra == 'fin':
            break

        for i in palabra:
            if i == letra:
                contadorLetra += 1

    print(f"La letra '{letra}' aparece {contadorLetra} veces en las palabras introducidas.")

letra = input("Introduce una letra: ")

contarLetraPalabras(letra)
