from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('el usuario abre el sitio web de la floristería')
def step_impl(context):
    context.driver = webdriver.Chrome() 
    context.driver.get("https://floristeriamundoflor.com")
    context.driver.maximize_window()
    time.sleep(3)

@when('navega a la categoría "Agradecimientos"')
def step_impl(context):
    time.sleep(3)
    agradecimientos = context.driver.find_element(By.XPATH, "//*[@id='menu-item-2794']/a")
    agradecimientos.click()
    time.sleep(5)

@when('agrega primer producto al carrito')
def step_impl(context):
    botones_agregar = context.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div[1]/div/div[1]/figure/a/img")
    context.driver.execute_script("window.scrollTo(0, 200);")
    botones_agregar.click()
    time.sleep(4)
    

@when('agrega segundo producto al carrito')
def step_impl(context):
    botones_agregar = context.driver.find_element(By.XPATH, "//*[@id='product-4079']/div/div[2]/div/form/div/input[3]")
    context.driver.execute_script("window.scrollTo(0, 200);")
    botones_agregar.click()
    time.sleep(3)
    
@when('agregar al carrito')
def step_impl(context):
    actualizacion_carrito = context.driver.find_element(By.NAME, "add-to-cart")
    context.driver.execute_script("window.scrollTo(0, 200);")

    actualizacion_carrito.click()
    time.sleep(3)
    

@then('los productos deben aparecer en el carrito')
def step_impl(context):
    productos_carrito = context.driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div/div[2]/div/div/div/div[2]/form/div/table/tbody/tr[1]/td[4]/div/input[2]")
    context.driver.execute_script("window.scrollTo(0, 100);")
    time.sleep(3)
    context.driver.quit()
