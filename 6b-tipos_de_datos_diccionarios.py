persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print(persona["nombre"])  # Imprime "Ana"

persona["edad"] = 31  # Cambia el valor de la clave "edad"
print(persona)  # Imprime {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid'}

print(len(persona))  # Imprime 3

persona["profesion"] = "programadora"  # Agrega una nueva clave
print(persona)  # Imprime {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'programadora'}

persona.pop("ciudad")  # Elimina la clave "ciudad"
print(persona)  # Imprime {'nombre': 'Ana', 'edad': 31, 'profesion': 'programadora'}

print(persona.keys())  # Imprime dict_keys(['nombre', 'edad', 'profesion'])

print(persona.values())  # Imprime dict_values(['Ana', 31, 'programadora'])

print(persona.items())  # Imprime dict_items([('nombre', 'Ana'), ('edad', 31), ('profesion', 'programadora')])

persona.clear()  # Elimina todos los elementos
print(persona)  # Imprime {}
