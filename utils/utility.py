import os
from datetime import datetime


def capture_screenshot(driver, folder="evidencias"):
    """Guarda un screenshot del estado actual del navegador.
    El nombre del archivo incluye timestamp para evitar sobrescritura.
    Retorna la ruta completa del archivo generado.

    Args:
        driver: Instancia de WebDriver (Chrome).
        folder: Carpeta donde guardar la imagen (por defecto 'evidencias').
    """
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"screenshot_{timestamp}.png")
    driver.save_screenshot(path)
    return path
