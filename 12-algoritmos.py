def encontrar_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# Ejemplo de uso
numeros = [3, 7, 2, 9, 5]
print("El número más grande es:", encontrar_mayor(numeros))