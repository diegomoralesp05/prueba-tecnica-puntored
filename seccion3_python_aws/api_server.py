from flask import Flask, jsonify
import pandas as pd
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Ruta del archivo por proveedor (simulado para 'A')
PROVEEDORES = ['A', 'B', 'C']

@app.route('/api/proveedor/<proveedor_id>', methods=['GET'])
def get_resumen(proveedor_id):
    if proveedor_id not in PROVEEDORES:
        logging.warning(f"Proveedor no válido: {proveedor_id}")
        return jsonify({"error": "Proveedor no válido"}), 400

    filename = os.path.join(os.path.dirname(__file__), f"resumen_proveedor_{proveedor_id}.json")
    if not os.path.exists(filename):
        logging.error(f"Archivo no encontrado: {filename}")
        return jsonify({"error": "Archivo no encontrado"}), 404

    try:
        data = pd.read_json(filename)
        logging.info(f"Datos cargados correctamente para proveedor {proveedor_id}")
        return jsonify(data.to_dict(orient="records"))
    except Exception as e:
        logging.exception("Error al leer el archivo JSON")
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
