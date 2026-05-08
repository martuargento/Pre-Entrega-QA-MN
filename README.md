# QA Automation - SauceDemo Testing

## Propósito del Proyecto

Este proyecto implementa pruebas automatizadas para el sitio web SauceDemo (https://www.saucedemo.com/), una aplicación de e-commerce de demostración. Las pruebas cubren funcionalidades clave como:

- Login exitoso
- Navegación y verificación del catálogo de productos
- Interacción con el carrito de compras

El objetivo es demostrar habilidades en automatización de pruebas QA utilizando herramientas modernas de testing.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Selenium WebDriver**: Para automatización de navegador web
- **pytest**: Framework de testing para Python
- **webdriver-manager**: Gestión automática de drivers de navegador
- **Chrome Browser**: Navegador utilizado para las pruebas

## Instalación de Dependencias

### Prerrequisitos

- Python 3.7 o superior instalado
- Google Chrome browser instalado

### Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias Python ejecutando:

pip install selenium pytest webdriver-manager


O si preferis usar el archivo requirements.txt:

pip install -r requirements.txt


## Ejecución de las Pruebas

Para ejecutar todas las pruebas, abrir la terminal y ejecutar el siguiente comando estando en la raíz del proyecto:

pytest tests


### Generar Reporte HTML

Para generar un reporte HTML de los resultados de las pruebas y guardarlo dentro de la carpeta "reporte":

pytest tests --html=reporte/reporte.html --self-contained-html


Nota: no tenes que borrar la carpeta "reporte" antes de ejecutar el comando.

