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
