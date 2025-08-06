Feature: Agregar productos de agradecimientos al carrito

  Scenario: Añadir dos productos de agradecimientos al carrito
    Given el usuario abre el sitio web de la floristería
    When navega a la categoría "Agradecimientos"
    And agrega primer producto al carrito
    And agrega segundo producto al carrito
    And agregar al carrito
    Then los productos deben aparecer en el carrito
