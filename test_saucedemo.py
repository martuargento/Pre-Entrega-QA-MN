import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_saucedemo, get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# 1) AUTOMATIZACION DE LOGIN
def test_login_exitoso(driver):
    login_saucedemo(driver)

    #► testeamos que la url actual sea "/inventory.html", indicando que fue exitoso el login
    assert "/inventory.html" in driver.current_url

    #hacemos una espera explicita hasta que el selector del titulo sea visible 
    #y guardamos el texto de ese elemento en la variable titulo
    titulo_principal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'app_logo'))
    ).text

    #► testeamos que el titulo sea 'Swag Labs'
    assert titulo_principal == 'Swag Labs'


    #hacemos lo mismo con el titulo de products
    titulo_products = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'title'))
    ).text

    #► testeamos que sea 'Products'
    assert titulo_products == 'Products'


# 2) NAVEGACION Y VERIFICACION DEL CATALOGO DE PRODUCTOS
def test_catalogo(driver):
    login_saucedemo(driver)

    #Verificamos que el titulo en en /inventory.html sea 'Products'
    titulo_products = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'title'))
    ).text

    #► testeamos que sea 'Products'
    assert titulo_products == 'Products'


    #hacemos una espera explicita hasta que todos los elementos con la clase 'inventory_item' sean visibles
    #que son los productos basicamente, y los guardamos en la variable products
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
    )

    print(f"Cantidad de productos en el catalogo: {len(products)}")

    #► testeamos que la cantidad de productos en el catalogo sea mayor a 0
    assert len(products) > 0


    filtro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'producto_sort_container'))
    )

    #testeamos que el filtro de orden de productos sea visible
    assert filtro.is_displayed()

    menu_hamburguesa = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'react_burger_menu_btn'))
    )

    #testeamos que el menu hamburguesa sea visible
    assert menu_hamburguesa.is_displayed()



# 3) INTERACCION CON EL CARRITO DE COMPRAS
def test_carrito(driver):
    login_saucedemo(driver)

    #volvemos a guardar todos los productos en products
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
    )

    #► aseguramos que haya productos antes de continuar
    assert len(products) > 0 

    #hacemos click en el boton de agregar al carrito del primer producto
    #(aca cumplimos con "Añadir un producto al carrito haciendo clic en el botón correspondiente")
    
    products[0].find_element(By.TAG_NAME, 'button').click() 

    #guardamos el titulo del producto agregado para validar luego que sea el mismo que aparece en el carrito
    titulo_del_producto_a_agregar = products[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
    

    #esperamos que el elemento del contador del carrito tenga el texto '1' y guardamos ese valor en la variable contador_del_carrito
    contador_del_carrito = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'shopping_cart_badge'), '1')
    )

    #► testeamos que el contador del carrito tenga el valor '1'
    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    carrito_de_compras = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_link'))
    )

    #hacemos click en el carrito de compras para ir a la pagina del carrito
    carrito_de_compras.click()

    #► testeamos que estamos en la url del carrito
    assert "/cart.html" in driver.current_url

    producto_agregado_en_el_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name'))
    )
    
    #► testeamos que el producto añadido sea el que habiamos seleccionado
    assert producto_agregado_en_el_carrito.text == titulo_del_producto_a_agregar


