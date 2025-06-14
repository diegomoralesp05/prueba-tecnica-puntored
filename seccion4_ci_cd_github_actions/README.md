# Sección 4 - CI/CD con GitHub Actions

Se implementa un pipeline de integración continua (CI) usando GitHub Actions para validar la calidad del código del proyecto.

## 🧪 ¿Qué hace este pipeline?

Cada vez que se hace un `push` o un `pull request` sobre la rama `main`, se ejecuta automáticamente:

1. Instalar dependencias:

   * Python 3.10
   * Flask, Pandas, Pytest

2. **Validar la sintaxis** de los scripts en `seccion3_python_aws`.

3. **Ejecutar pruebas automatizadas** ubicadas en la carpeta `tests/`.

4. **Simular la generación de documentación automática**.

---

## 🧩 Estructura de archivos

```
.github/
└── workflows/
    └── ci.yml        # Archivo de configuración del pipeline CI/CD

seccion4_ci_cd/
├── README.md             # Este archivo explicativo
└── logs_pipeline.txt     # Logs de ejecución exitosa del pipeline

tests/
└── test_dummy.py         # Prueba de ejemplo (usando pytest)
```

---

## ▶️ ¿Cómo ejecutarlo?

1. `push` a la rama `main` (o crea un `pull request`)

```bash
git add .
git commit -m "Cambios"
git push origin main
```

2. Ir al repositorio en GitHub → pestaña **Actions**

3. Seleccionar el workflow **CI Pipeline** para ver los logs paso a paso

---

## logs

* el archivo `logs_pipeline.txt` con la salida completa del pipeline ejecutado correctamente


