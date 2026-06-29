import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from utils.utility import capture_screenshot


def before_scenario(context, scenario):
    """Configura el navegador Chrome antes de cada escenario.
    - Si HEADLESS=0 se ejecuta con ventana visible (util para depuracion).
    - Por defecto corre en modo headless para ejecucion batch.
    """
    chrome_options = Options()
    # TODO: revisar si en linux esto funciona sin --headless
    if os.environ.get("HEADLESS", "1") != "0":
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 30)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


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
