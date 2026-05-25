# Sistema de detección de noticias falsas

Sistema web que analiza noticias y predice si son verdaderas o falsas mediante Inteligencia Artificial, Procesamiento de Lenguaje Natural (NLP) y Machine Learning.

## Descripción

El usuario puede ingresar una noticia de dos formas: pegando el texto directamente o proporcionando una URL. El sistema limpia el texto, lo transforma con TF-IDF y aplica un modelo de Regresión Logística entrenado con los datasets FakeNewsNet e ISOT. La predicción se muestra en una interfaz web desarrollada en Flask.

## Tecnologías utilizadas

- **Lenguaje:** Python 3.11+
- **Machine Learning:** scikit-learn (TF-IDF, Regresión Logística)
- **Procesamiento de texto:** NLTK
- **Web scraping:** requests, BeautifulSoup, Trafilatura
- **Framework web:** Flask
- **Manejo de datos:** pandas, numpy
- **Persistencia del modelo:** joblib

## Estructura del proyecto

```
fake-news-detection/
├── app/                 # Aplicación Flask
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/       # Archivos HTML
│   └── static/          # CSS e imágenes
├── data/                # Datasets
│   ├── raw/             # Datasets sin procesar
│   └── processed/       # Datasets limpios
├── models/              # Modelos entrenados
├── scraping/            # Módulo de extracción web
│   ├── __init__.py
│   └── extractor.py
├── notebooks/           # Jupyter notebooks
├── tests/               # Pruebas unitarias
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
└── run.py
```

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/usuario/fake-news-detection.git
cd fake-news-detection
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
python run.py
```

Luego abrir el navegador en `http://localhost:5000`.

## Equipo de desarrollo

| Integrante | Rol | Responsabilidad |
|------------|-----|-----------------|
| Mauricio Coca | Investigación, NLP y modelo | Datasets, TF-IDF, entrenamiento y métricas |
| Israel Mollo | Flask y frontend | Interfaz web, formularios y visualización |
| Dari Lopez | Scraping e integración | Extracción de URLs e integración del sistema |

## Cronograma

| Sprint | Fecha | Enfoque |
|--------|-------|---------|
| Sprint 0 | 22/05/2026 | Validación con cliente |
| Sprint 1 | 25/05/2026 | Base del producto |
| Sprint 2 | 29/05/2026 | Limpieza de datos |
| Sprint 3 | 01/06/2026 | Entrenamiento del modelo |
| Sprint 4 | 08/06/2026 | Integración con Flask |
| Sprint 5 | 12/06/2026 | Scraping y mejoras |
| Sprint 6 | 15-19/06/2026 | Integración final |

## Datasets

- **FakeNewsNet:** repositorio con noticias de PolitiFact y GossipCop.
- **ISOT Fake News Dataset:** corpus de noticias verdaderas (Reuters) y falsas.

## Licencia

Proyecto académico desarrollado con fines educativos.
