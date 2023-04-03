import serial
import time
import pandas as pd

# Configuración del puerto serial
ser = serial.Serial("/dev/ttyACM0", 460800)

# Crear una lista para almacenar los datos recibidos
datos = []

# Crear una variable cuenta para almacenar un número determinado de datos
var_count = 0
muestras_total = 10000#int(input("Cuantas muestras deseas? "))

# Leer datos del puerto serial y agregar a la lista hasta que se presione ingresan todos los datos deseados
tiempo_actual = 0.0  # tiempo actual
while var_count<muestras_total:
    # Leer una línea de datos del puerto serial y decodificarla
    linea_datos = ser.readline().decode().strip()
    # Dividir los datos por el guión "-"
    datos_separados = linea_datos.split("-")
    # Obtener el ADC y DAC de los datos separados
    adc = (float)(datos_separados[0])/4095
    dac = (float)(datos_separados[1])
    # Agregar los datos y el tiempo a la lista
    datos.append([round(tiempo_actual,3), adc, dac])
    # Incrementar el tiempo en 0.001 ms
    tiempo_actual += 0.001
    var_count += 1

# Cerrar el puerto serial
ser.close()

# Convertir la lista de datos en un DataFrame de pandas
df = pd.DataFrame(datos, columns=['TIEMPO', 'ADC', 'DAC'])

# Guardar los datos en un archivo CSV con la columna de tiempo
df.to_csv('Data_Nucleo2.csv', index=False)

print("CSV Creado \n")