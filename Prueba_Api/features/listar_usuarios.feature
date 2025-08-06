Feature: Listar usuarios
  Scenario: Obtener lista de usuarios en la página 2
    Given que el servicio de reqres está disponible
    When envío una solicitud GET al endpoint "/api/users?page=2"
    Then el código de respuesta debe ser 200
    And la respuesta debe contener una lista de usuarios