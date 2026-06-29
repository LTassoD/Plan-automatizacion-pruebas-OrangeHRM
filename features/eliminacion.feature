Feature: Eliminación de empleados

  @Caso8
  Scenario Outline: Visualizar lista de empleados
    Given el usuario ha iniciado sesión correctamente
    When navega a PIM > Employee List
    Then la tabla de empleados debe mostrar datos
    And se captura screenshot con timestamp

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
