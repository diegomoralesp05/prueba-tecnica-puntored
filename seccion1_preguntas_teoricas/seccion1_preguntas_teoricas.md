## Sección 1: Preguntas Teóricas

### Python 

**1. ¿Cuál es la diferencia entre una lista y un conjunto (set) en Python? Proporcione un ejemplo.**

* Una lista es una estructura ordenada que permite elementos duplicados.
* Un conjunto (set) es una colección desordenada que no permite duplicados.

```python
lista = [1, 2, 2, 3]
conjunto = set(lista)
print(lista)    # [1, 2, 2, 3]
print(conjunto) # {1, 2, 3}
```

**2. ¿Qué es un generator en Python y en qué casos es útil? Proporcione un ejemplo de implementación.**

* Es una función que usa `yield` para devolver valores uno a uno.
* Se utiliza cuando se necesita eficiencia en memoria al manejar grandes volúmenes de datos.

```python
def contador():
    for i in range(1000000):
        yield i

for numero in contador():
    print(numero)
```

**3. ¿Qué ventajas ofrece Pandas sobre las estructuras de datos nativas de Python para el análisis de datos?**

* Mayor eficiencia en operaciones vectorizadas.
* Métodos integrados para limpieza, transformación y análisis.
* Fácil integración con fuentes de datos y herramientas externas.
* Manejo eficiente de datos tabulares con funciones como `groupby`, `merge`, y `pivot_table`.

**4. ¿Cuál es la diferencia entre apply() y map() en Pandas? Proporcione un ejemplo.**

* `apply()` funciona con Series y DataFrames, permite aplicar funciones complejas.
* `map()` solo funciona con Series, más limitado pero útil para transformaciones simples.

```python
import pandas as pd

df = pd.DataFrame({'nombre': ['Ana', 'Luis'], 'edad': [25, 30]})

# apply sobre columna de un DataFrame
df['edad_cuadrado'] = df['edad'].apply(lambda x: x**2)

# map sobre Serie
df['nombre_mayus'] = df['nombre'].map(str.upper)
```

### SQL

**1. Consulta para obtener el salario promedio de cada departamento, incluyendo el nombre del departamento.**

```sql
SELECT d.nombre AS nombre_departamento, AVG(e.salario) AS salario_promedio
FROM empleados e
JOIN departamentos d ON e.departamento_id = d.id
GROUP BY d.nombre;
```

**2. Diferencia entre INNER JOIN, LEFT JOIN y FULL JOIN. Ejemplo de cada uno.**

* `INNER JOIN`: devuelve solo las filas que tienen coincidencias en ambas tablas.
* `LEFT JOIN`: devuelve todas las filas de la tabla izquierda y las coincidencias de la derecha.
* `FULL JOIN`: devuelve todas las filas de ambas tablas, incluso sin coincidencias.

```sql
-- INNER JOIN
SELECT * FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

-- LEFT JOIN
SELECT * FROM empleados e
LEFT JOIN departamentos d ON e.departamento_id = d.id;

-- FULL JOIN (PostgreSQL)
SELECT * FROM empleados e
FULL JOIN departamentos d ON e.departamento_id = d.id;
```

**3. ¿Cómo optimizarías una consulta en una base de datos con millones de registros?**

* Crear índices en columnas utilizadas en filtros, joins o agrupamientos.
* Usar particionamiento de tablas si aplica.
* Evitar `SELECT *`, preferir solo columnas necesarias.
* Analizar el plan de ejecución (`EXPLAIN` o `EXPLAIN ANALYZE`).
* Filtrar lo más posible antes de hacer joins o agrupamientos.

**4. ¿Qué es la cláusula HAVING en SQL y en qué se diferencia de WHERE?**

* `WHERE` filtra filas **antes del agrupamiento** (`GROUP BY`).
* `HAVING` filtra **después del agrupamiento**.

```sql
-- WHERE antes del GROUP BY
SELECT * FROM ventas WHERE monto > 100;

-- HAVING después del GROUP BY
SELECT cliente_id, SUM(monto) AS total
FROM ventas
GROUP BY cliente_id
HAVING SUM(monto) > 1000;
```

### Amazon Web Services

**1. Diferencia entre Amazon S3, Amazon RDS y Amazon Redshift.**

* **Amazon S3**: almacenamiento de objetos escalable. Ideal para archivos, logs, backups.
* **Amazon RDS**: base de datos relacional administrada (MySQL, PostgreSQL, etc.).
* **Amazon Redshift**: base de datos analítica columnar para procesamiento masivo de datos (OLAP).

**2. ¿Cuándo usarías Amazon DynamoDB en lugar de RDS o Redshift?**

* Cuando se necesita latencia de milisegundos, escalabilidad automática y un modelo NoSQL (clave-valor o documentos).
* Ej: Aplicaciones móviles, juegos, IoT o cargas con acceso impredecible.

**3. Diferencias entre AWS Lambda y EC2 para ejecutar cargas de trabajo.**

* **AWS Lambda**:

  * Serverless, paga por ejecución.
  * Ideal para tareas pequeñas o eventos (automatizaciones, APIs).
* **AWS EC2**:

  * Proporciona máquinas virtuales.
  * Control total del entorno, más apto para procesos largos o sistemas personalizados.

**4. ¿Cómo implementarías un mecanismo seguro para que un servicio en AWS acceda a un bucket de S3 sin usar claves de acceso en el código?**

* Utilizar **IAM Roles** con permisos asignados.
* Si es una Lambda, asociar el rol directamente al servicio.
* Definir políticas mínimas necesarias para acceso.
* Ejemplo: una política que permita `s3:GetObject` solo en un prefijo específico del bucket.

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::mi-bucket/proveedor1/*"
}
```
