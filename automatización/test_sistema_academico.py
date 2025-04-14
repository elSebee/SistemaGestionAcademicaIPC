from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------
# FUNCIONES DE UTILIDAD
# -----------------------
def cargar_datos():
    datos = {}
    with open("datos_automatizacion.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split("=")
            datos[clave] = valor.split(",") if "," in valor else valor
    return datos


def setup_driver():
    options = EdgeOptions()
    options.add_experimental_option("detach", True)
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(5)
    return driver


def login(driver, password):
    driver.get("http://localhost:3006/")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[text()='Entrar']")
    login_button.click()


# -----------------------
# CASOS DE PRUEBA
# -----------------------
def test_login(password):
    driver = setup_driver()
    login(driver, password)
    time.sleep(2)
    assert "#" in driver.current_url, "Error: No se redireccionó correctamente"
    print("F-001: Inicio de sesión exitoso.")
    driver.quit()


def test_search_student(password, alumnos, nombres):
    driver = setup_driver()
    login(driver, password)
    time.sleep(2)

    for rut, nombre in zip(alumnos, nombres):
        search_bar = driver.find_element(By.XPATH, "//input[@type='text']")
        search_bar.clear()
        search_bar.send_keys(rut)
        search_bar.send_keys(Keys.RETURN)

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        search_button.click()
        print("Búsqueda realizada.")

        student_info = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'a[href="#/estudiante/{rut}"]'))
        )
        student_name = student_info.find_element(By.CSS_SELECTOR, '.text-lg')
        assert nombre in student_name.text, f"Error: No se encontró al estudiante {rut}."
        print(f"F-002: Búsqueda exitosa de {nombre}.")

        time.sleep(2)

    driver.quit()


# -----------------------
# EJECUCIÓN DE PRUEBAS
# -----------------------
datos = cargar_datos()
test_login(datos["password"])
test_search_student(datos["password"], datos["alumnos"], datos["nombres"])
