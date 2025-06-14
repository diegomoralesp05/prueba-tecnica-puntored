# Sección 4 - CI/CD con GitHub Actions

Este módulo implementa un pipeline de integración continua (CI) usando **GitHub Actions** para validar la calidad del código del proyecto.

## 🧪 ¿Qué hace este pipeline?

Cada vez que haces un `push` o un `pull request` sobre la rama `main`, se ejecuta automáticamente:

1. **Instala dependencias:**

   * Python 3.10
   * Flask, Pandas, Pytest

2. **Valida la sintaxis** de los scripts en `seccion3_python_aws`.

3. **Ejecuta pruebas automatizadas** ubicadas en la carpeta `tests/`.

4. **Simula la generación de documentación automática** (puedes integrar herramientas reales como `pdoc` o `Sphinx`).

---

## 🧩 Estructura de archivos

```
.github/
└── workflows/
    └── ci.yml        # Archivo de configuración del pipeline CI/CD

seccion4_ci_cd/
└── README.md         # Este archivo explicativo

tests/
└── test_dummy.py     # Prueba de ejemplo (usando pytest)
```

---

## ▶️ ¿Cómo ejecutarlo?

1. Haz `push` a la rama `main` (o crea un `pull request`)

```bash
git add .
git commit -m "Cambios"
git push origin main
```

2. Ve a tu repositorio en GitHub → pestaña **Actions**

3. Selecciona el workflow **CI Pipeline** para ver los logs paso a paso

---

## 📸 Captura o logs

Puedes tomar una **captura de pantalla** del pipeline en ejecución o copiar y pegar los logs desde GitHub Actions.

---

## 🔧 Extensiones futuras

* Integración con `pdoc` o `mkdocs` para documentación real
* Despliegue automático a entornos de prueba
* Notificaciones por Slack o correo
