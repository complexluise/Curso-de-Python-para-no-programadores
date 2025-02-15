frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # Accede al primer elemento: "manzana"

frutas[1] = "naranja"  # Cambia el segundo elemento
print(frutas)  # Imprime ['manzana', 'naranja', 'cereza']

print(len(frutas))  # Imprime 3

frutas.append("uva")  # Agrega un elemento al final
print(frutas)  # Imprime ['manzana', 'naranja', 'cereza', 'uva']

frutas.pop(1)  # Elimina el segundo elemento
print(frutas)  # Imprime ['manzana', 'cereza', 'uva']

print(frutas[1:])  # Imprime ['cereza', 'uva']
