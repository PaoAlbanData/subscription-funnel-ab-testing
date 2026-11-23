"""Carga de la configuración del proyecto desde config/config.yaml."""

from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
CONFIG_PATH: Path = PROJECT_ROOT / "config" / "config.yaml"


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    """Lee el archivo YAML de configuración y lo devuelve como diccionario.

    Args:
        path: Ruta al archivo de configuración. Por defecto, config/config.yaml.

    Returns:
        Diccionario con las secciones del archivo (project, paths, simulation, experiment).

    Raises:
        FileNotFoundError: Si el archivo de configuración no existe.
    """
    if not path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo de configuración: {path}")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def project_path(relative: str) -> Path:
    """Convierte una ruta relativa de la configuración en una ruta absoluta del proyecto.

    Args:
        relative: Ruta relativa a la raíz del proyecto (p. ej. "data/raw").

    Returns:
        Ruta absoluta dentro del proyecto.
    """
    return PROJECT_ROOT / relative
