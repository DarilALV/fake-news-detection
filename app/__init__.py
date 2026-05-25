"""
Inicializacion de la aplicacion Flask.
"""

from flask import Flask


def create_app(config_name="default"):
    """Crea y configura la aplicacion Flask."""
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Registrar las rutas
    from app.routes import main
    app.register_blueprint(main)

    return app
