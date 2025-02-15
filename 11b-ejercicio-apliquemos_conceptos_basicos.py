# TODO: Crear un diccionario vacío para almacenar los estudiantes y sus notas
estudiantes = {}

# TODO: Pedir al usuario cuántos estudiantes registrará
num_estudiantes = int(input("¿Cuántos estudiantes deseas registrar? "))

# Bucle para ingresar los datos de cada estudiante
for i in range(num_estudiantes):
    # TODO: Pedir al usuario el nombre del estudiante
    nombre = input(f"\nIngresa el nombre del estudiante {i + 1}: ")
    
    # TODO: Pedir las notas separadas por comas y convertirlas en una lista de números
    print("Las notas son sobre 100")
    notas = input(f"Ingrese las notas de {nombre}, separadas por comas: ")
    lista_notas = [int(nota) for nota in notas.split(",")]  # <--- Completar recuerda que debe ser una lista de números
    
    # Guardar en el diccionario
    estudiantes[nombre] = lista_notas

# TODO: Mostrar los resultados de cada estudiante
print("\nResultados:")
promedio_total = 0

for nombre, notas in estudiantes.items():
    # TODO: Calcular el promedio sumando las notas y dividiéndolas entre la cantidad
    promedio = sum(notas) / len(notas)  # <--- Completar recuerda que el promedio es la suma de las notas entre la cantidad de notas
    
    # TODO: Determinar si el estudiante aprobó (mínimo 60)
    if promedio >= 60:
        estado = "Aprobado"  # Si la condición se cumple, el estado es?
    else:
        estado = "No aprobado"  # Si la condición no se cumple, el estado es?
    
    print(f"{nombre} - Promedio: {promedio:.2f} - Estado: {estado}")
    
    # Acumular promedio total para la clase
    promedio_total = promedio + promedio_total

# TODO: Calcular y mostrar el promedio general de la clase
promedio_clase = promedio_total / len(estudiantes)  # <--- Completar
print(f"\nPromedio general de la clase: {promedio_clase:.2f}")
