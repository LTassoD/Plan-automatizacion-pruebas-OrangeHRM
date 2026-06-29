Feature: Actualización de perfil My Info

  @Caso13
  Scenario Outline: Navegar y verificar My Info
    Given el usuario ha iniciado sesión correctamente
    When navega a My Info
    Then la página de My Info debe cargar correctamente
    And se captura screenshot como evidencia

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
