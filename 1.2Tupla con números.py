numeros = (3, 5, 8, 3, 9, 5, 3, 1, 8, 7, 5)

while True:
    numero_buscado = int(input("Introdusca un numero (Precione 0 para salir): "))
    
    if numero_buscado == 0:
        print("Saliendo del programa.")
        break
    
    repeticiones = numeros.count(numero_buscado)
    
    print(f"El número {numero_buscado} se repite {repeticiones} veces en la tupla.")
