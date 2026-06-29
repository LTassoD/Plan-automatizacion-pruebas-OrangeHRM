Feature: Login y Validación de Acceso Orange HRM

  @Caso1
  Scenario: 1. Login exitoso + screenshot
    When ingresa usuario "Admin" y contraseña "admin123"
    And hace clic en el botón Login
    Then debería ver el dashboard
    And se captura screenshot con timestamp

  @Caso2
  Scenario: 2. Login con credenciales inválidas + screenshot
    When ingresa usuario "invalido" y contraseña "invalida"
    And hace clic en el botón Login
    Then debería ver un mensaje de error
    And se captura screenshot con timestamp

  @Caso4
  Scenario: 4. Assert falla en verificación de título
    When ingresa usuario "Admin" y contraseña "admin123"
    And hace clic en el botón Login
    Then el título debe ser "OrangeHRM OS 5.7"

  Scenario: 10. Validar campos obligatorios en login
    When deja los campos de usuario y contraseña vacíos
    And hace clic en el botón Login
    Then debería ver mensajes de validación
