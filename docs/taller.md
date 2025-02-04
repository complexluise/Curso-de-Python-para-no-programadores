## **Python para no programadoras**

## Parte 1: Bienvenida y Contexto

### ¿Qué es Python?
Python es un lenguaje de programación popular, conocido por su facilidad de uso y sintaxis clara. Es utilizado en diversas áreas como desarrollo web, análisis de datos, inteligencia artificial y automatización de tareas.

Python es un lenguaje ideal para principiantes porque:
- Su sintaxis es intuitiva y fácil de leer.
- Tiene una gran comunidad de soporte.
- Se usa en muchas industrias y aplicaciones.

### ¿Qué aprenderemos en este taller?
En este taller, cubriremos los conceptos básicos de Python y veremos aplicaciones prácticas que nos ayudarán a resolver problemas del día a día con ayuda de la inteligencia artificial.

Al finalizar este taller, serás capaz de:
- Comprender la sintaxis básica de Python.
- Escribir funciones y algoritmos sencillos.
- Usar herramientas para automatizar tareas como generar códigos QR, cortar videos y unir PDFs.

## Parte 2: Introducción a Python

### 1. Instalación y Configuración (Opcional, si aplica)
Para escribir y ejecutar código en Python, podemos usar:
- **Google Colab** (recomendado para este taller, ya que no requiere instalación).
- **Jupyter Notebook** (parte de Anaconda, si deseas instalar Python en tu computadora).
- **Python IDLE o Visual Studio Code** (para un entorno más avanzado).

Si estás usando Google Colab, solo necesitas una cuenta de Google y acceder a [Colab](https://colab.research.google.com/).

### 2. Sintaxis Básica de Python
Python usa una sintaxis limpia y sencilla. Veamos algunos ejemplos:

#### Variables y Tipos de Datos
```python
# Declarar variables en Python
nombre = "Ana"
edad = 25
altura = 1.65
es_estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)
```

**Explicación:**
- `nombre` es una cadena de texto (string).
- `edad` es un número entero (int).
- `altura` es un número decimal (float).
- `es_estudiante` es un valor booleano (True o False).

#### Estructuras de Control: Condicionales
```python
# Uso de if-else
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

**Explicación:**
- `input()` permite recibir datos del usuario.
- `int()` convierte la entrada en un número entero.
- `if` evalúa si la edad es 18 o mayor, de lo contrario ejecuta `else`.

#### Estructuras de Control: Bucles
```python
# Uso de un bucle for
for i in range(5):
    print("Iteración", i)

# Uso de un bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

**Explicación:**
- `for` recorre una secuencia de números con `range()`.
- `while` ejecuta un bloque de código mientras se cumpla una condición.

#### Listas y Diccionarios
```python
# Lista de números
numeros = [10, 20, 30, 40]
print("Primer elemento:", numeros[0])

# Diccionario de información
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print("Nombre:", persona["nombre"])
```

**Explicación:**
- Una **lista** es una colección ordenada de elementos.
- Un **diccionario** almacena pares clave-valor.

### 3. Ejercicio Práctico
Vamos a escribir un programa que pida el nombre de un usuario y lo salude.

```python
nombre = input("¡Hola! ¿Cuál es tu nombre? ")
print("Encantado de conocerte,", nombre, "!")
```

---

## Parte 3: Algoritmos y Funciones

### 1. ¿Qué es un Algoritmo?
Un **algoritmo** es un conjunto de pasos organizados que permiten resolver un problema o realizar una tarea. En programación, los algoritmos se implementan a través de código para automatizar procesos.

Ejemplo de un algoritmo simple: Calcular la suma de dos números.
```python
a = 10
b = 20
suma = a + b
print("La suma es:", suma)
```

### 2. Introducción a Funciones en Python
Las **funciones** nos permiten reutilizar código y estructurar mejor nuestros programas.

#### Declaración y Uso de Funciones
```python
# Definir una función
def saludar(nombre):
    print("Hola,", nombre, "¡Bienvenido al curso de Python!")

# Llamar a la función
saludar("Ana")
```

**Explicación:**
- `def` se usa para definir una función.
- `nombre` es un parámetro que recibe un valor cuando se llama la función.
- `print()` muestra el mensaje en pantalla.

#### Funciones con Retorno de Valores
```python
# Función que suma dos números y devuelve el resultado
def sumar(a, b):
    return a + b

resultado = sumar(5, 7)
print("El resultado de la suma es:", resultado)
```

**Explicación:**
- `return` permite devolver un valor al programa.
- Podemos almacenar el valor devuelto en una variable.

### 3. Ejercicio Práctico
Escribe una función que reciba una lista de números y devuelva la suma de los números pares.
```python
def sumar_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

numeros = [1, 2, 3, 4, 5, 6]
print("Suma de números pares:", sumar_pares(numeros))
```
### **Parte 4: Uso de IA para Resolver Problemas Cotidianos**  

La inteligencia artificial (IA) y la automatización nos permiten simplificar tareas repetitivas y optimizar el tiempo. En esta sección, aprenderemos a utilizar Python para trabajar con **archivos PDF**, generando herramientas prácticas que nos permitan manipular estos documentos de manera eficiente.  

---

### **1. Trabajar con PDFs en Python**  
Los archivos PDF son muy utilizados para compartir información en un formato seguro y estandarizado. Sin embargo, muchas veces necesitamos **modificarlos, combinarlos o extraer información** de ellos.  

Para esto, utilizaremos la biblioteca [`pypdf`](https://pypi.org/project/pypdf/), que nos permite:  
✅ **Unir varios PDFs en un solo archivo.**  
✅ **Dividir un PDF en múltiples archivos.**  
✅ **Extraer texto de un PDF.**  
✅ **Rotar páginas dentro de un PDF.**  

Antes de comenzar, si aún no tienes instalada la biblioteca, puedes instalarla con el siguiente comando:  
```bash
pip install pypdf
```

Ahora revisemos la documentación para conocer las funcionalidades [documentación pypdf](https://pypdf.readthedocs.io/en/stable/)

---

### **2. Unir Múltiples PDFs**  
Supongamos que tenemos varios archivos PDF y queremos unirlos en un solo documento. Podemos hacerlo con el siguiente código:

```python
from pypdf import PdfMerger

# Crear un objeto de combinación
merger = PdfMerger()

# Agregar múltiples archivos PDF
pdfs = ["archivo1.pdf", "archivo2.pdf", "archivo3.pdf"]
for pdf in pdfs:
    merger.append(pdf)

# Guardar el PDF combinado
merger.write("resultado.pdf")
merger.close()

print("PDFs combinados exitosamente en 'resultado.pdf'")
```

📌 **Explicación:**  
- Creamos un objeto `PdfMerger()`.  
- Usamos `append()` para añadir cada archivo a la fusión.  
- Guardamos el resultado en `resultado.pdf`.  

---

### **3. Dividir un PDF en Varias Partes**  
En ocasiones, necesitamos extraer páginas específicas de un documento. Con `PyPDF2`, podemos dividir un PDF en archivos más pequeños:

```python
from pypdf import PdfReader, PdfWriter

# Cargar el PDF de origen
pdf = PdfReader("documento.pdf")

# Crear un nuevo PDF con ciertas páginas
pdf_writer = PdfWriter()
paginas_a_extraer = [0, 2, 4]  # Índices de las páginas a extraer (empiezan desde 0)

for pagina in paginas_a_extraer:
    pdf_writer.add_page(pdf.pages[pagina])

# Guardar el nuevo archivo PDF
with open("documento_recortado.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)

print("Se ha creado 'documento_recortado.pdf' con las páginas seleccionadas.")
```

📌 **Explicación:**  
- `PdfReader` carga el documento original.  
- `PdfWriter` permite escribir un nuevo PDF con solo las páginas seleccionadas.  
- `add_page()` copia las páginas que especificamos.  
- Guardamos el archivo nuevo con `write()`.  

---

### **4. Extraer Texto de un PDF**  
A veces necesitamos recuperar el contenido de un documento para analizarlo o modificarlo. Podemos hacer esto con `PyPDF2` de la siguiente manera:

```python
from pypdf import PdfReader

# Cargar el PDF
pdf = PdfReader("documento.pdf")

# Extraer el texto de todas las páginas
texto_completo = ""
for pagina in pdf.pages:
    texto_completo += pagina.extract_text() + "\n"

# Guardar el texto en un archivo
with open("texto_extraido.txt", "w", encoding="utf-8") as archivo_texto:
    archivo_texto.write(texto_completo)

print("Texto extraído y guardado en 'texto_extraido.txt'")
```

📌 **Explicación:**  
- `PdfReader` abre el PDF.  
- Iteramos sobre `pdf.pages` para extraer texto con `extract_text()`.  
- Guardamos el contenido en un archivo de texto.  

---

### **5. Rotar Páginas en un PDF**  
Si tienes páginas mal orientadas en un documento, puedes corregirlas girándolas 90, 180 o 270 grados:

```python
from pypdf import PdfReader, PdfWriter

# Cargar el PDF
pdf = PdfReader("documento.pdf")
pdf_writer = PdfWriter()

# Rotar todas las páginas 90 grados
for pagina in pdf.pages:
    pagina.rotate(90)  # Se puede usar 90, 180 o 270 grados
    pdf_writer.add_page(pagina)

# Guardar el nuevo archivo
with open("documento_rotado.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)

print("Se ha creado 'documento_rotado.pdf' con las páginas rotadas.")
```

📌 **Explicación:**  
- `rotate(90)` rota cada página 90 grados.  
- `PdfWriter` guarda el resultado en un nuevo archivo.  

---

### **6. Creación de una Herramienta Útil**  
Hemos visto diferentes funciones para manejar archivos PDF. Ahora, podemos combinarlas en un solo **script interactivo** para que el usuario elija qué acción realizar:

```python
def menu():
    print("Herramienta de Manipulación de PDFs")
    print("1. Unir PDFs")
    print("2. Dividir un PDF")
    print("3. Extraer texto de un PDF")
    print("4. Rotar páginas de un PDF")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Código para unir PDFs
        pass
    elif opcion == "2":
        # Código para dividir PDFs
        pass
    elif opcion == "3":
        # Código para extraer texto
        pass
    elif opcion == "4":
        # Código para rotar páginas
        pass
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
```

Este script presenta un **menú interactivo** donde el usuario puede seleccionar qué acción realizar con sus PDFs.

Ahora integremos todo para tener una herramienta funcional.

```python
import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def unir_pdfs():
    """Une múltiples archivos PDF en uno solo"""
    pdfs = input("Ingresa los nombres de los PDFs a unir (separados por coma): ").split(",")

    merger = PdfMerger()
    for pdf in pdfs:
        pdf = pdf.strip()
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"El archivo {pdf} no existe, se omitirá.")

    salida = input("Ingresa el nombre del archivo de salida (ejemplo: resultado.pdf): ")
    merger.write(salida)
    merger.close()
    print(f"Los archivos han sido combinados en {salida}")

def dividir_pdf():
    """Divide un PDF extrayendo páginas seleccionadas"""
    archivo = input("Ingresa el nombre del PDF a dividir: ")
    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return

    pdf = PdfReader(archivo)
    pdf_writer = PdfWriter()
    
    paginas = input("Ingresa los números de página a extraer (ejemplo: 0,2,4): ")
    paginas = [int(p.strip()) for p in paginas.split(",")]

    for pagina in paginas:
        if pagina < len(pdf.pages):
            pdf_writer.add_page(pdf.pages[pagina])
        else:
            print(f"La página {pagina} no existe en el documento.")

    salida = input("Ingresa el nombre del archivo de salida (ejemplo: documento_dividido.pdf): ")
    with open(salida, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Se ha creado '{salida}' con las páginas seleccionadas.")

def extraer_texto():
    """Extrae el texto de un PDF y lo guarda en un archivo de texto"""
    archivo = input("Ingresa el nombre del PDF a extraer texto: ")
    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return

    pdf = PdfReader(archivo)
    texto_completo = ""

    for pagina in pdf.pages:
        texto_completo += pagina.extract_text() + "\n"

    salida = input("Ingresa el nombre del archivo de texto de salida (ejemplo: texto_extraido.txt): ")
    with open(salida, "w", encoding="utf-8") as archivo_texto:
        archivo_texto.write(texto_completo)

    print(f"El texto ha sido extraído y guardado en '{salida}'")

def rotar_paginas():
    """Rota todas las páginas de un PDF en el ángulo deseado"""
    archivo = input("Ingresa el nombre del PDF a rotar: ")
    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return

    pdf = PdfReader(archivo)
    pdf_writer = PdfWriter()

    angulo = int(input("Ingresa el ángulo de rotación (90, 180, 270): "))
    if angulo not in [90, 180, 270]:
        print("Ángulo no válido. Debe ser 90, 180 o 270.")
        return

    for pagina in pdf.pages:
        pagina.rotate(angulo)
        pdf_writer.add_page(pagina)

    salida = input("Ingresa el nombre del archivo de salida (ejemplo: documento_rotado.pdf): ")
    with open(salida, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Se ha creado '{salida}' con las páginas rotadas {angulo} grados.")

def menu():
    """Muestra el menú de opciones"""
    while True:
        print("\n--- HERRAMIENTA DE MANIPULACIÓN DE PDFs ---")
        print("1. Unir PDFs")
        print("2. Dividir un PDF")
        print("3. Extraer texto de un PDF")
        print("4. Rotar páginas de un PDF")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            unir_pdfs()
        elif opcion == "2":
            dividir_pdf()
        elif opcion == "3":
            extraer_texto()
        elif opcion == "4":
            rotar_paginas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar la herramienta
menu()
```

Para usarla abrimos la terminal y ejecutamos.
```bash
python maneja_pdfs.py
```

### **Parte 5: Cierre y Preguntas**  

Hemos llegado al final del taller, donde hemos explorado desde los conceptos básicos de Python hasta la creación de una herramienta funcional para manipular archivos PDF. En esta última sección, haremos un repaso general, daremos recomendaciones para continuar aprendiendo y responderemos dudas.  

---

### **📌 Recapitulación de lo Aprendido**  
Durante este taller, hemos cubierto los siguientes temas:  

✅ **Introducción a Python**: Sintaxis, variables, estructuras de control y colecciones de datos.  
✅ **Algoritmos y Funciones**: Cómo escribir funciones reutilizables y estructurar código de manera eficiente.  
✅ **Uso de IA para Resolver Problemas**: Implementamos herramientas prácticas para manipular archivos PDF.  
✅ **Creación de una Herramienta Completa**: Diseñamos un programa interactivo que permite unir, dividir, extraer texto y rotar archivos PDF.  

Con estos conocimientos, ahora tienes una base sólida para seguir explorando Python y su potencial en el mundo real. 🚀  

---

### **📖 Recomendaciones para Seguir Aprendiendo Python**  

El aprendizaje de la programación es un proceso continuo. Aquí tienes algunas recomendaciones para seguir avanzando:  

📚 **Recursos en línea gratuitos**  
- **[Python para Todos](https://automatetheboringstuff.com/)** – Un excelente libro para aprender a automatizar tareas con Python.  
- **[Real Python](https://realpython.com/)** – Tutoriales detallados y cursos sobre diversos temas.  
- **[W3Schools Python](https://www.w3schools.com/python/)** – Explicaciones sencillas y ejercicios prácticos.  
- **[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/#toc)** - Un libro increible donde se muestran los conceptos esenciales para empezar a automatizar en python.

👨‍💻 **Práctica con Proyectos Reales**  
- **Automatización de Tareas**: Usa Python para organizar archivos, enviar correos automáticos o extraer datos de la web.  
- **Análisis de Datos**: Explora bibliotecas como `pandas` y `matplotlib` para manejar y visualizar datos.  
- **Desarrollo Web**: Aprende sobre `Flask` o `Django` para crear aplicaciones web.  

🛠 **Plataformas para Practicar y Retar tus Habilidades**  
- **[HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-python)** – Desafíos y ejercicios con soluciones explicadas.  
- **[LeetCode](https://leetcode.com/)** – Retos de algoritmos y estructuras de datos.  
- **[Kaggle](https://www.kaggle.com/)** – Competencias y datasets para análisis de datos e inteligencia artificial.  

📢 **Participa en Comunidades**  
- **Grupos en Discord y Telegram** sobre Python.  
- **Foros como Stack Overflow y Reddit** (`r/learnpython`) para resolver dudas y aprender de otros.  
- **Eventos y meetups locales** donde puedes conocer programadores con intereses similares.  

---

### **🎤 Espacio de Preguntas y Reflexión**  
Antes de concluir, abrimos un espacio para responder preguntas y compartir experiencias:  
- ¿Qué te ha parecido el taller?  
- ¿Qué tema te resultó más interesante o desafiante?  
- ¿Tienes ideas para aplicar Python en tu vida o trabajo?  

Finalmente, recuerda que aprender a programar no es cuestión de talento, sino de **práctica y constancia**. Sigue explorando, experimentando y divirtiéndote con Python. ¡Este es solo el comienzo! 🚀💡  

---

**¡Gracias por participar y nos vemos en el próximo taller!** 🎉