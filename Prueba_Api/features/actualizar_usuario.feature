Feature: Actualizar usuario existente
  Scenario: Actualizar el nombre y trabajo del usuario
    Given que el servicio de reqres está disponible
    When envío una solicitud PUT al endpoint "/api/users/2" con el cuerpo:
      """
      {
        "name": "Andres",
        "job": "Automation Engineer"
      }
      """
    Then el código de respuesta debe ser 200
    And la respuesta debe contener el campo "updatedAt"
