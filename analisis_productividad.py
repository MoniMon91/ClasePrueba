import pandas as pd

# Leer archivo Excel (debe estar en la misma carpeta)
archivo = 'productividad_equipo.xlsx'
datos = pd.read_excel(archivo)

# Calcular productividad
datos['Productividad'] = datos['Unidades Producidas'] / datos['Horas Trabajadas']

# Mostrar la tabla con productividad
print("📊 Productividad por empleado:\n")
print(datos[['Empleado', 'Productividad']])