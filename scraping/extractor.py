"""
Modulo de extraccion de contenido desde URLs de noticias.

Este modulo se desarrollara completamente en el Sprint 5.
Por ahora, contiene la estructura base.
"""

import requests
from bs4 import BeautifulSoup
import trafilatura

from config import SCRAPING_TIMEOUT, USER_AGENT, MIN_TEXT_LENGTH


def is_valid_url(url):
    """Valida que la URL tenga un formato correcto."""
    if not url:
        return False
    return url.startswith("http://") or url.startswith("https://")


def fetch_html(url):
    """Descarga el HTML de una URL."""
    if not is_valid_url(url):
        raise ValueError("URL invalida")

    headers = {"User-Agent": USER_AGENT}

    try:
        response = requests.get(url, headers=headers, timeout=SCRAPING_TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        raise TimeoutError("El sitio tardo demasiado en responder")
    except requests.exceptions.HTTPError as e:
        raise ConnectionError(f"Error al acceder a la URL: {e}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Error de conexion: {e}")


def extract_with_trafilatura(html):
    """Extrae el contenido principal usando Trafilatura."""
    return trafilatura.extract(html)


def extract_with_beautifulsoup(html):
    """Extrae el contenido principal usando BeautifulSoup como respaldo."""
    soup = BeautifulSoup(html, "lxml")

    # Buscar etiquetas comunes que contienen el cuerpo del articulo
    for tag in ["article", "main"]:
        element = soup.find(tag)
        if element:
            return element.get_text(separator=" ", strip=True)

    # Si no encontramos nada, devolver todo el texto
    return soup.get_text(separator=" ", strip=True)


def extract_article(url):
    """Funcion principal: extrae el contenido limpio de una noticia."""
    html = fetch_html(url)

    # Intentar con Trafilatura primero
    content = extract_with_trafilatura(html)

    # Si Trafilatura falla, usar BeautifulSoup como respaldo
    if not content:
        content = extract_with_beautifulsoup(html)

    if not content or len(content.split()) < MIN_TEXT_LENGTH:
        raise ValueError("El contenido extraido es muy corto o esta vacio")

    return content
