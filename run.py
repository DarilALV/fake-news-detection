"""
Punto de entrada de la aplicacion Flask.

Para ejecutar:
    python run.py

La aplicacion estara disponible en http://localhost:5000
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
