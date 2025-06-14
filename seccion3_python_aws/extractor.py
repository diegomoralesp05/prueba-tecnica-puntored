import pandas as pd
from datetime import datetime, timedelta

# Este script usa un DataFrame simulado en lugar de conectarse a PostgreSQL

# Producto del proveedor (por ejemplo, proveedor1 tiene producto 'A')
PRODUCTO_PROVEEDOR = 'A'

# Fecha simulada
fecha_actual = datetime.now().date()
fecha_objetivo = fecha_actual - timedelta(days=1)

# Datos simulados
datos_ventas = pd.DataFrame({
    'cliente_id': [1, 1, 2, 2, 3, 1],
    'fecha': [
        fecha_objetivo, fecha_objetivo,
        fecha_objetivo, fecha_actual,
        fecha_objetivo, fecha_objetivo
    ],
    'monto': [100.0, 150.0, 200.0, 300.0, 250.0, 50.0],
    'producto': ['A', 'B', 'A', 'A', 'A', 'A']
})

# Filtrar por fecha objetivo y producto del proveedor
filtro = (
    (datos_ventas['fecha'] == fecha_objetivo) &
    (datos_ventas['producto'] == PRODUCTO_PROVEEDOR)
)

ventas_filtradas = datos_ventas[filtro]

# Agrupar por cliente y fecha
resultado = ventas_filtradas.groupby(['cliente_id', 'fecha']) \
    .agg(cantidad_transacciones=('monto', 'count'),
         monto_total=('monto', 'sum')) \
    .reset_index()

# Añadir campo de proveedor
resultado['proveedor'] = PRODUCTO_PROVEEDOR

# Reordenar columnas
resultado = resultado[['proveedor', 'fecha', 'cliente_id', 'cantidad_transacciones', 'monto_total']]

# Guardar en JSON en formato requerido por el proveedor
archivo_salida = f"resumen_proveedor_{PRODUCTO_PROVEEDOR}.json"
resultado.to_json(archivo_salida, orient="records", date_format="iso", force_ascii=False, indent=2)

print("Extracción completada. Datos guardados en JSON:", archivo_salida)

# Mostrar resultado en consola
print(resultado)
