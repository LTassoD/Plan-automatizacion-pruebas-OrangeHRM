Feature: Gestión de Sesión (Logout)

  @Caso3
  Scenario: 3. Logout exitoso + screenshot
    Given el usuario ha iniciado sesión correctamente
    When hace clic en el menú de usuario
    And selecciona la opción Logout
    Then debería redirigirse a la página de login
    And se captura screenshot con timestamp
