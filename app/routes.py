"""
Rutas de la aplicacion Flask.

Sprint 1: solo se muestra la pantalla inicial.
La logica de prediccion se implementara en sprints posteriores.
"""

from flask import Blueprint, render_template, request, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Pantalla principal del sistema."""
    return render_template("index.html")


@main.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint de prediccion.
    
    Sprint 1: devuelve un mensaje informativo.
    Sprint 3: se conectara al modelo entrenado.
    Sprint 4: integracion completa con el flujo real.
    """
    text = request.form.get("text", "").strip()
    url = request.form.get("url", "").strip()

    if not text and not url:
        return jsonify({
            "status": "error",
            "message": "Debe ingresar un texto o una URL"
        }), 400

    return jsonify({
        "status": "pending",
        "message": "El modelo estara disponible a partir del Sprint 3",
        "sprint": 1,
        "received": {
            "text_length": len(text),
            "url": url if url else None
        }
    })


@main.route("/health")
def health():
    """Verificacion de estado de la aplicacion."""
    return jsonify({
        "status": "ok",
        "sprint": 1,
        "version": "0.1.0"
    })
