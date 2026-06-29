Feature: Búsqueda de empleados con filtros

  @Caso6
  Scenario Outline: Buscar empleado por nombre y estado
    Given el usuario ha iniciado sesión correctamente
    When navega a PIM > Employee List
    And aplica filtros de la fila <NroFila> del Excel
    And hace clic en el botón Search
    Then los resultados deben coincidir con lo esperado
    And se captura screenshot con timestamp

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
