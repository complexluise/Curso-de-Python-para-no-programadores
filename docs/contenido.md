## **Python para no programadorxs**

### **Objetivos del Taller**
1. Introducir los fundamentos básicos de Python.
2. Explicar y aplicar conceptos de algoritmos y funciones.
3. Demostrar cómo usar la IA para resolver problemas cotidianos y construir una herramienta para manejar PDFs.

---

### **Estructura del Taller**

#### **1. Bienvenida y Contexto (5 minutos)**
- Presentación del instructor.
- Breve introducción a Python y su popularidad en diversas industrias.
- Enfoque del taller: Aprender Python básico + Aplicaciones prácticas con IA.

---

#### **2. Introducción a Python (20 minutos)**

**Contenido:**
- ¿Qué es Python?
- Instalar Python y Jupyter Notebook/Google Colab (solo mencionar, ya configurado para el taller).  
- Conceptos básicos:  
  - Sintaxis básica y variables.
  - Tipos de datos: números, cadenas, listas, diccionarios.
  - Estructuras de control: `if` y `for`. Solo hacer mención de `while`, pero no profundizar.
  - Entrada y salida: `input()` y `print()`. 

**Ejercicio Rápido:**
Escribir un programa que pida la edad del usuario y diga si es mayor o menor de edad.

---

#### **3. Algoritmos y Funciones (20 minutos)**

**Contenido:**
- ¿Qué es un algoritmo? Ejemplo básico.
- Funciones en Python:  
  - Definición y uso (`def`).  
  - Parámetros y valores de retorno.  
  - Funciones predefinidas vs personalizadas.
- Ejemplo práctico:  
  Escribir una función que reciba una lista de números y devuelva la suma de los números pares.  

**Ejercicio Guiado:**
Crear una función que reciba un nombre y devuelva un saludo personalizado.

---

#### **4. Uso de IA para Resolver Problemas Cotidianos (40 minutos)**

**4.1 Herramientas de IA para Programar (10 minutos)**
- Mostrar cómo usar herramientas como ChatGPT (u otras AI) para:
  - Generar código.
  - Explicar conceptos complejos.
  - Solucionar errores.

**4.2 Manipulación de PDFs con Python (30 minutos)**
- Introducción a `PyPDF2`.
- **Unir múltiples PDFs en un solo archivo:**
  - Explicación y código de ejemplo para combinar varios archivos PDF en uno solo.

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.write("merged.pdf")
merger.close()
```

- **Dividir un PDF en varios archivos más pequeños:**
  - Código para extraer páginas específicas de un documento y guardarlas en archivos independientes.

- **Extraer texto de un PDF:**
  - Código que permite recuperar texto de un archivo PDF y guardarlo en un documento de texto.

- **Rotar páginas en un PDF:**
  - Código para modificar la orientación de las páginas dentro de un documento PDF.

- **Hagamos nuestra herramienta para manejar PDFs:**
  - Con todo lo aprendido en el taller hagamos una interfaz básica para poder usar nuestra herramienta.

---

#### **5. Cierre y Preguntas (5 minutos)**
- Recapitulación de lo aprendido.
- Recomendaciones para seguir aprendiendo Python.
- Espacio para preguntas y respuestas.
- Agradecimientos y despedida.

---


### **Material Adicional para los Participantes**
- Acceso al código usado durante el taller en Github.
- CheatSheets con lo visto en clase

- Lista de recursos para aprender Python:
  - Documentación oficial de Python.
  - Tutoriales en línea: W3Schools, Real Python, etc.
- `pypdf`
-[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/#toc)
