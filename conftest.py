import pytest
import os
from utils.helpers import get_driver


#este fixture es el que va a usar cada test para tener un navegador chrome abierto y 
#controlado por selenium webdriver:
@pytest.fixture(scope="function") 
def driver():
    driver = get_driver()  #utilizamos get_driver() que es donde se produce el chrome abierto y controlado por selenium
    yield driver
    driver.quit()

# creamos un hook para detectar fallos guardar los screenshoots
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield #ejecutamos el test y esperamos el resultado del mismo
    reporte = outcome.get_result() #obtenemos si paso o no, y lo guardamos en la variable reporte


    if reporte.when == "call" and reporte.failed:     # si fue un fallo real de test
        driver = item.funcargs.get('driver') # conseguimos el navegador del test que fallo, y lo guardamos
        if driver:
            # creamos la carpeta de screenshots si no existe
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # tomamos la captura de pantalla
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Captura guardada en {screenshot_path}")