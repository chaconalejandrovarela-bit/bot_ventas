# ============================================
# NUEVO ANALISIS - agregar en la rama "mejoras"
# ============================================

# Pregunta 6: Precio promedio de venta por categoria
precio_promedio_categoria = df_consolidado.groupby('categoria')['precio_unitario'].mean()
print("Precio promedio por categoria:")
print(precio_promedio_categoria)

# Pregunta 7: Cantidad de transacciones por vendedor
transacciones_por_vendedor = df_consolidado.groupby('vendedor')['precio_unitario'].count()
print("Cantidad de transacciones por vendedor:")
print(transacciones_por_vendedor)

# Guardar este analisis extra en un nuevo archivo
resumen_extra = pd.DataFrame({
    'precio_promedio': precio_promedio_categoria
})
resumen_extra.to_excel("analisis_extra.xlsx")
