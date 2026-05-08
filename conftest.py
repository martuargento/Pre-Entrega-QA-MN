import pytest
import os
from utils.helpers import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # ejecutar todos los otros hooks para obtener el objeto de reporte
    outcome = yield
    rep = outcome.get_result()

    # solo miramos las llamadas de pruebas que fallan realmente, no setup/teardown
    if rep.when == "call" and rep.failed:
        # obtenemos el driver del elemento de la prueba
        driver = item.funcargs.get('driver')
        if driver:
            # creamos la carpeta de screenshots si no existe
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # tomamos la captura de pantalla
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Captura guardada en {screenshot_path}")