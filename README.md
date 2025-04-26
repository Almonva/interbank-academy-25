# 💳 Procesamiento de Transacciones Bancarias (CLI)

## 🧩 Introducción

Este proyecto consiste en una aplicación desarrollada en Python. El objetivo principal es procesar un archivo CSV con transacciones bancarias (de tipo "Crédito" o "Débito") y generar un reporte útil para el usuario.  
Este reto forma parte de la formación en Interbank Academy 25.

---

## ⚙️ Instrucciones de Ejecución


   ### 1. Clona el repositorio en local

   git clone https://github.com/Almonva/interbank-academy-25
   cd interbank-academy-25

   ### 2. Crea y activa un entorno virtual desde el terminal

   python -m venv venv
   venv\Scripts\activate

   ### 3. Ejecutamos el script desde terminal

python main.py

## 🧠 Enfoque y Solución

La aplicación fue diseñada para procesar un archivo CSV con transacciones bancarias y generar un reporte con tres métricas:

   1. **Balance Final:** La lógica suma los montos de las transacciones de tipo "Crédito" y resta los montos de las transacciones de tipo "Débito". Esto se logra de manera simple recorriendo cada fila del archivo CSV y actualizando el saldo según el tipo de transacción.

   2. **Transacción de Mayor Monto:** A medida que se recorren las filas del archivo, se compara el monto de cada transacción con el monto más alto encontrado hasta el momento. Si una transacción tiene un monto mayor, se actualiza el ID y el monto de la transacción de mayor valor.

   3. **Conteo de Transacciones:** Se lleva un conteo de las transacciones de tipo "Crédito" y "Débito" utilizando un diccionario por las claves de cada tipo. Este conteo se incrementa cada vez que se procesa una transacción de cada tipo.

   ### Decisiones de Diseño:
   - **Uso de `csv.DictReader`:** Utilicé `csv.DictReader` para leer el archivo CSV, lo que permite acceder a cada columna utilizando nombres de columna. 
   
   - **Uso de diccionarios:** Para mantener un seguimiento de las transacciones, usé diccionarios para almacenar el conteo de tipos de transacciones y la transacción de mayor monto.

   - **Manejo de tipos de datos:** Convertí los valores de monto y transacción a tipos numéricos (`float` para los montos y `int` para los IDs) para poder realizar las operaciones y las comparaciones necesarias segun el tipo necesario.

## 🗂️ Estructura del Proyecto

A continuación se describe la estructura principal:

   ### Descripción de Archivos y Carpetas:

   - **`data.csv`**: Este es el archivo de entrada que contiene las transacciones bancarias en formato CSV. Cada línea tiene un ID, un tipo de transacción ("Crédito" o "Débito"), y un monto asociado. Este archivo es procesado por el script principal.

   - **`main.py`**: El script principal que contiene la lógica del programa. Lee el archivo `data.csv`, procesa las transacciones, calcula el balance final, encuentra la transacción de mayor monto y cuenta el número de transacciones de cada tipo, luego imprime un reporte en la terminal.

   - **`.gitignore`**: Este archivo contiene las configuraciones necesarias para evitar que Git suba archivos y carpetas innecesarias al repositorio, como el entorno virtual `venv` o archivos temporales del sistema operativo.

   - **`README.md`**: Este archivo, que contiene la documentación del proyecto, incluyendo la introducción, instrucciones de ejecución, enfoque, solución y detalles de la estructura del proyecto.

   - **`venv/`**: La carpeta que contiene el entorno virtual. Esta carpeta no se subio a Git y contiene las dependencias necesarias para ejecutar el proyecto.



