"""
Configuracion general del proyecto Fake News Detection.
"""

import os
from pathlib import Path

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"

# Configuracion de Flask
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave-de-desarrollo-cambiar-en-produccion")
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

# Configuracion del modelo
MODEL_FILENAME = "logistic_regression_model.pkl"
VECTORIZER_FILENAME = "tfidf_vectorizer.pkl"

# Configuracion del scraping
SCRAPING_TIMEOUT = 10  # segundos
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
MIN_TEXT_LENGTH = 50  # palabras minimas para una prediccion confiable

# Datasets
FAKENEWSNET_FILES = {
    "politifact_fake": "politifact_fake.csv",
    "politifact_real": "politifact_real.csv",
    "gossipcop_fake": "gossipcop_fake.csv",
    "gossipcop_real": "gossipcop_real.csv",
}

ISOT_FILES = {
    "true": "True.csv",
    "fake": "Fake.csv",
}
