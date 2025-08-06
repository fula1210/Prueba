Feature: Eliminar usuario existente
  Scenario: Eliminar el usuario con ID 2
    Given que el servicio de reqres está disponible
    When envío una solicitud DELETE al endpoint "/api/users/2"
    Then el código de respuesta debe ser 204
