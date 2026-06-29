Feature: Solicitud de licencias

  @Caso14
  Scenario Outline: Navegar a Leave Apply
    Given el usuario ha iniciado sesión correctamente
    When navega a Leave > Apply
    Then la página de solicitud de licencia debe cargar correctamente
    And se captura screenshot con timestamp

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
