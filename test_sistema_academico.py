from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Inicializa y devuelve una instancia del WebDriver de Microsoft Edge."""
    options = EdgeOptions()
    options.add_experimental_option("detach", True)  # Para evitar que se cierre automáticamente
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(5)  # Espera implícita
    return driver

def test_login():
    """Caso de prueba F-001: Inicio de sesión exitoso."""
    driver = setup_driver()
    driver.get("http://localhost:3006/")
    
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("1234")
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Entrar']")
    login_button.click()
    
    time.sleep(3)
    
    assert "#" in driver.current_url, "Error: No se redireccionó correctamente"
    print("F-001: Inicio de sesión exitoso.")
    driver.quit()

def test_search_student():
    """Caso de prueba F-002: Búsqueda de un estudiante existente por RUT."""
    driver = setup_driver()
    driver.get("http://localhost:3006/")

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("1234")
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Entrar']")
    login_button.click()
    
    search_bar = driver.find_element(By.XPATH, "//input[@type='text']")
    search_bar.send_keys("21015358-6")
    search_bar.send_keys(Keys.RETURN)

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    search_button.click()
    print("Búsqueda realizada.")


    student_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="#/estudiante/21015358-6"]'))
    )

    student_name = student_info.find_element(By.CSS_SELECTOR, '.text-lg')
    assert "MUÑOZ CORONADO FELIPE ALEJANDRO SEB" in student_name.text, "Error: No se encontró al estudiante."
    print("F-002: Búsqueda de estudiante exitosa.")
    
    time.sleep(2)
    search_bar.clear()

    search_bar = driver.find_element(By.XPATH, "//input[@type='text']") 
    search_bar.send_keys("20244190-4")
    search_bar.send_keys(Keys.RETURN)

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')) 
    )
    search_button.click()
    print("Búsqueda realizada.")
    
    student_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="#/estudiante/20244190-4"]'))
    )

    student_name = student_info.find_element(By.CSS_SELECTOR, '.text-lg')
    assert "GOMEZ FRIZ NICOLAS MOISES ANTONIO" in student_name.text, "Error: No se encontró al estudiante."
    print("F-002: Búsqueda de estudiante exitosa.")
    
    time.sleep(2)

    driver.quit()

test_login()
test_search_student()
