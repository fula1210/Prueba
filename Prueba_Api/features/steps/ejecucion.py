import requests
from behave import given, when, then

@given('que el servicio de reqres está disponible') 
def step_impl(context):
    context.base_url = "https://reqres.in"

@when('envío una solicitud GET al endpoint "/api/users?page=2"')
def step_impl(context):
    url = f"{context.base_url}/api/users?page=2"
    context.response = requests.get(url)

@then('el código de respuesta debe ser 200')
def step_impl(context):
    assert context.response.status_code == 200, \
        f"Código esperado: 200, pero fue {context.response.status_code}"

@then('la respuesta debe contener una lista de usuarios')
def step_impl(context):
    data = context.response.json()
    assert "data" in data, "La clave 'data' no está en la respuesta"
    assert isinstance(data["data"], list), "La clave 'data' no contiene una lista"
    assert len(data["data"]) > 0, "La lista de usuarios está vacía"
