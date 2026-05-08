from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# configuramos logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
    logger.info("Inicializando el driver de Chrome")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    logger.info("Driver de Chrome inicializado exitosamente")
    return driver


def login_saucedemo(driver):
    logger.info("Iniciando proceso de login en la web Saucedemo")
    driver.get(URL)
    logger.info(f"Navegando a {URL}")

    driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()
    logger.info("Credenciales enviadas y botón de login clickeado")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
    )
    logger.info("Login exitoso - Página de inventario cargada")
