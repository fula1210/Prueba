Feature: Crear nuevo usuario
  Scenario: Crear un usuario con nombre y trabajo
    Given que el servicio de reqres está disponible
    When envío una solicitud POST al endpoint "/api/users" con el cuerpo:
      """
      {
        "name": "Juan",
        "job": "QA"
      }
      """
    Then el código de respuesta debe ser 201
    And la respuesta debe contener el campo "id" y "createdAt"
