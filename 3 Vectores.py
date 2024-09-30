def calcular_media(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def contar_temperaturas_superiores(temperaturas, media):
    contador = 0
    for temp in temperaturas:
        if temp >= media:
            contador += 1
    return contador

n = int(input("Ingrese el número de temperaturas a promediar: "))
temperaturas = []

for i in range(n):
    temp = float(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temp)

media = calcular_media(temperaturas)

temperaturas_superiores = contar_temperaturas_superiores(temperaturas, media)

print(f"\nLa media de las temperaturas es: {media:.2f}")
print(f"El número de temperaturas mayores o iguales a la media es: {temperaturas_superiores}")

input("\nPresione Enter para finalizar el programa...")
