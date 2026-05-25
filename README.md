# Sistema de detección de noticias falsas

Sistema web que analiza noticias y predice si son verdaderas o falsas mediante Inteligencia Artificial, Procesamiento de Lenguaje Natural (NLP) y Machine Learning.

![Sprint 1](https://img.shields.io/badge/Sprint-1%2F6-blue) ![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow) ![Python](https://img.shields.io/badge/Python-3.11+-green)

## Descripción

El usuario puede ingresar una noticia de dos formas: pegando el texto directamente o proporcionando una URL. El sistema limpia el texto, lo transforma con TF-IDF y aplica un modelo de Regresión Logística entrenado con los datasets FakeNewsNet e ISOT. La predicción se muestra en una interfaz web desarrollada en Flask.

## Estado actual: Sprint 1 (25/05/2026)

**Entregables completados:**
- Repositorio en GitHub con estructura organizada
- Aplicación Flask base con pantalla inicial funcional
- Investigación y exploración de datasets (notebook `01_investigacion_datasets.ipynb`)
- Módulo de scraping con estructura base lista
- Dependencias documentadas y configuración base

**Próximos sprints:**
- Sprint 2 (29/05): Limpieza y preparación de datos
- Sprint 3 (01/06): Entrenamiento del modelo TF-IDF + Regresión Logística
- Sprint 4 (08/06): Integración del modelo con Flask
- Sprint 5 (12/06): Implementación del scraping y mejoras
- Sprint 6 (15-19/06): Estabilización, pruebas y demo final

## Tecnologías

- **Lenguaje:** Python 3.11+
- **Machine Learning:** scikit-learn (TF-IDF, Regresión Logística)
- **Procesamiento de texto:** NLTK
- **Web scraping:** requests, BeautifulSoup, Trafilatura
- **Framework web:** Flask
- **Manejo de datos:** pandas, numpy
- **Visualización:** matplotlib, seaborn

## Estructura del proyecto

```
fake-news-detection/
├── app/                      # Aplicación Flask
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── data/                     # Datasets (ignorados por git)
│   ├── raw/
│   └── processed/
├── models/                   # Modelos entrenados (ignorados por git)
├── scraping/                 # Módulo de extracción web
│   ├── __init__.py
│   └── extractor.py
├── notebooks/                # Análisis y experimentación
│   └── 01_investigacion_datasets.ipynb
├── tests/                    # Pruebas unitarias
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
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
python run.py
```

Abrir en el navegador: `http://localhost:5000`

## Datasets utilizados

### ISOT Fake News Dataset (Principal)
- **Tamaño:** ~44,898 noticias (21,417 verdaderas + 23,481 falsas)
- **Idioma:** Inglés
- **Fuente:** University of Victoria
- **Columnas usadas:** `text` (entrada), `label` (etiqueta)

### FakeNewsNet (Complementario)
- **Contenido:** Noticias de PolitiFact y GossipCop
- **Limitación:** El acceso público solo incluye CSVs con metadatos.

## Equipo de desarrollo

| Integrante | Rol | Responsabilidad |
|------------|-----|-----------------|
| Mauricio Coca | Investigación, NLP y modelo | Datasets, TF-IDF, entrenamiento y métricas |
| Israel Mollo | Flask y frontend | Interfaz web, formularios y visualización |
| Dari Lopez | Scraping e integración | Extracción de URLs e integración del sistema |

## Cómo ejecutar el sistema

Una vez instaladas las dependencias:

```bash
python run.py
```

La aplicación estará disponible en `http://localhost:5000`. En este Sprint 1, la interfaz está completa pero la predicción real estará operativa a partir del Sprint 3.

## Licencia

Proyecto académico desarrollado con fines educativos. La Paz, Bolivia — 2026.
