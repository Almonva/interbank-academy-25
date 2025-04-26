# Importe de librería de lectura de archivos .csv
import csv

# Definición de función de procesamiento de transacciones
def procesar_transacciones(ruta_csv):
    # Inicializamos el balance en 0
    balance = 0.0

    # Creamos contadores para las transacciones de tipo Crédito y Débito
    conteo = {"Crédito": 0, "Débito": 0}

    # Creamos un diccionario para guardar la transacción con el monto más alto
    transac_mayor = {"id": None, "monto": 0.0}

    # Abrimos el archivo CSV, usando UTF-8 para la lectura de los acentos
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        # Creamos un lector con DictReader para que cada fila sea un diccionario según los encabezados
        lector = csv.DictReader(archivo)

        # Recorremos cada fila del archivo
        for fila in lector:
            # Obtenemos el tipo de transacción
            tipo = fila["tipo"]

            # Obtenemos el monto y lo convertimos a número decimal con float
            monto = float(fila["monto"])

            # Obtenemos el ID de la transacción como número entero con Int
            transac_id = int(fila["id"])

            # Si es un Crédito, sumamos el monto al balance y aumentamos el contador
            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1

            # Si es un Débito, restamos el monto del balance y aumentamos su contador
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            # Verificamos si esta transacción tiene el monto mas alto por cada recorrido
            if monto > transac_mayor["monto"]:
                transac_mayor["id"] = transac_id
                transac_mayor["monto"] = monto

    # Imprimimos el reporte final en la terminal
    print("Reporte de Transacciones")
    print("-" * 45)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {transac_mayor['id']} - {transac_mayor['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

# Variable para correr el archivo
if __name__ == "__main__":
    # Ejecutamos la función con el archivo CSV
    procesar_transacciones("data.csv")
