import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.utility import capture_screenshot


def before_scenario(context, scenario):
    """Configura el navegador Chrome antes de cada escenario.
    - Si HEADLESS=0 se ejecuta con ventana visible (util para depuracion).
    - Por defecto corre en modo headless para ejecucion batch.
    """
    chrome_options = Options()
    if os.environ.get("HEADLESS", "1") != "0":
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    context.driver.set_page_load_timeout(60)
    context.wait = WebDriverWait(context.driver, 60)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.wait.until(EC.presence_of_element_located((By.NAME, "username")))


def after_scenario(context, scenario):
    """Limpia el navegador despues de cada escenario.
    - Si el escenario fallo, toma un screenshot automatico en la carpeta evidencias/.
    - Finaliza la sesion de Chrome.
    """
    if scenario.status == "failed":
        safe_name = "".join(c for c in scenario.name if c.isalnum() or c in (" ", "_")).strip()
        capture_screenshot(context.driver, "evidencias")
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
