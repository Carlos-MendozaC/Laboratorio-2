meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    numero = int(input("Introduce un número entre 1 y 12 (Precione 0 para salir): "))
 
    if numero == 0:
        print("Saliendo del programa.")
        break

    elif 1 <= numero <= len(meses):
        print(f"El mes correspondiente es: {meses[numero - 1]}")

    else:
        print("Número fuera de rango. Intenta de nuevo.")
