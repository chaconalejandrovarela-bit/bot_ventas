import pandas as pd
import glob 

# Exploración de los datos y diferentestipos de archivos 
# .csv y .xlsx

df_medellin = pd.read_csv("sucursal_medellin.csv")
#print(df_medellin.head(3))
#print("\n")
df_bogota = pd.read_excel("sucursal_bogota.xlsx")
#print(df_bogota.head(3))
#print(df_bogota.columns)
#print(df_medellin.columns)

# Agrupar archivos de ventas de diferentes sucursales en un solo DataFrame tipo .csv y .xlsx
archivos_csv = glob.glob("*.csv")
archivos_excel = glob.glob("*.xlsx")

print("Archivos CSV encontrados:", archivos_csv)
print("Archivos Excel encontrados:", archivos_excel)

# Unificar los archivos de ventas en un solo DataFrame

lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)
    print(f"Leídos: {archivo} - {len(df)} registros cargados con éxito.")

for archivo in archivos_excel:
    df = pd.read_excel(archivo)
    lista_informes.append(df)
    print(f"Leídos: {archivo} - {len(df)} registros cargados con éxito.")


# Unir todos los DataFrames en uno solo

df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(df_consolidado)

# Renombrar columnas para unificar los nombres de las columnas en los diferentes archivos
for i, df in enumerate(lista_informes):
    if 'Fecha_venta' in df.columns:
        lista_informes[i] = df.rename(columns={
            'Fecha_Venta': 'fecha' , "Producto": "producto", 
            "Categoria": "categoria",
            "Cant": "cantidad", "Valor_unitario": "precio_unitario",
            "Vendedor": "vendedor",
            "Pago": "Metodo_pago"   
        })
        
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(df_consolidado.columns)  # deberia mostrar exactamente 7
        
# --------------------------------------------
# PARTE 4: Limpieza de datos (NUEVO - hoy)
# --------------------------------------------

# 4a. Eliminar filas duplicadas
filas_antes = len(df_consolidado)
df_consolidado = df_consolidado.drop_duplicates()
print(f"Filas antes: {filas_antes} - despues: {len(df_consolidado)}")

# 4b. Explorar valores nulos ANTES de decidir que hacer
print(df_consolidado.isnull().sum())

# 4c. Rellenar segun el tipo de columna
# completar: decidan que valor tiene sentido para cada columna con nulos


# --------------------------------------------
# PARTE 5: Guardar el resultado
# --------------------------------------------
df_consolidado.to_excel("consolidado_limpio.xlsx", index=False)
print("Archivo guardado")

# ADVERTENCIA: si vuelven a ejecutar este script, glob va a 
# encontrar tambien "consolidado_limpio.xlsx" y tratar de leerlo 
# como si fuera un archivo de sucursal (dara error).
# Solucion: cambien el patron de busqueda arriba de "*.xlsx" a 
# "sucursal_*.xlsx", o guarden el resultado en una subcarpeta aparte.









