# Sección 3 - Extractor y API para Proveedores

Este módulo contiene dos scripts en Python que permiten extraer datos de ventas por proveedor desde una base de datos simulada y exponerlos mediante una API REST.

## Estructura de archivos

```
seccion3_python_aws/
├── extractor.py              # Extrae datos y genera archivo resumen_proveedor_*.json
├── api_server.py             # Servidor Flask para exponer los datos en formato JSON
├── resumen_proveedor_A.json # Archivo generado con resumen de ventas (ejemplo)
```

## Requisitos previos

* Python 3.7 o superior
* Instalar las dependencias necesarias:

```bash
pip install flask pandas
```

---

## Paso 1: Ejecutar el extractor de datos

Este script genera un archivo `.json` con la cantidad de transacciones y monto total por cliente, por día, filtrado por producto de proveedor.

```bash
cd seccion3_python_aws
python extractor.py
```

Este comando creará un archivo llamado, por ejemplo:

```
resumen_proveedor_A.json
```

---

## Paso 2: Levantar el servidor API

El servidor lee el archivo generado y lo expone en un endpoint por proveedor.

```bash
python api_server.py
```

### Endpoint disponible

```
GET /api/proveedor/<proveedor_id>
```

Ejemplo:

```
http://localhost:5000/api/proveedor/A
```

---

## Manejo de errores

* Si el proveedor no es válido, se retorna código `400`.
* Si el archivo no existe, se retorna `404`.
* Si ocurre un error interno, se retorna `500`.

---

## Próximos pasos

* Automatizar el pipeline con cron o AWS Lambda + EventBridge
* Publicar el API con AWS API Gateway
* Control de acceso por proveedor
