Feature: Edición de empleados

  @Caso7
  Scenario Outline: Editar empleado desde la lista
    Given el usuario ha iniciado sesión correctamente
    When navega a PIM > Employee List
    And hace clic en el botón Search
    Then la tabla de empleados debe mostrar datos
    And se captura screenshot con timestamp

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
