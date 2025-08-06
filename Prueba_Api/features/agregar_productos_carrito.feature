Feature: Agregar productos de agradecimientos al carrito
  Scenario: Añadir dos productos de agradecimientos al carrito
    Given el usuario está en la página principal
    When navega a la categoría "Agradecimientos"
    And añade dos productos al carrito
    Then los productos deben visualizarse en la opción "Carro"
