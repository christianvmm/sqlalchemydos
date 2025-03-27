import pandas as pd
import numpy as np


# Cargar el CSV
#df = pd.read_csv('hotel_bookings.csv')
#########################

# Guardar como Excel
#df.to_excel('hotel_bookings.xlsx', index=False, engine='openpyxl')  # Agrega el motor para evitar errores
#print("Archivo convertido a Excel con éxito.")
#########################

# Guardar como JSON
#df.to_json('hotel_bookings.json', orient='records', indent=4)
#print("Archivo convertido a JSON con éxito.")
###########################

#Esta parte del codigo es solo para inconsistencias de la base de datos
# Cargar el CSV original
df = pd.read_csv('hotel_bookings.csv')

# Introducir valores nulos
for _ in range(10):
    idx = np.random.randint(0, len(df))
    col = np.random.choice(df.columns)
    df.at[idx, col] = np.nan

# Introducir formatos de fecha inconsistentes
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], errors='coerce')
for _ in range(10):
    idx = np.random.randint(0, len(df))
    df.at[idx, 'reservation_status_date'] = f"{np.random.randint(1, 31)}-{np.random.randint(1, 12)}-{np.random.randint(2016, 2020)}"

# Guardar los archivos modificados
df.to_csv('hotel_bookings_inconsistent.csv', index=False)
df.to_excel('hotel_bookings_inconsistent.xlsx', index=False, engine='openpyxl')
df.to_json('hotel_bookings_inconsistent.json', orient='records', indent=4)

print("Archivos con inconsistencias generados.")