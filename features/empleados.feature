Feature: Registro de empleados Data-Driven

  @Caso5
  Scenario Outline: Agregar empleado con datos desde Excel
    Given el usuario ha iniciado sesión correctamente
    When navega a PIM > Add Employee
    And carga los datos del empleado de la fila <NroFila> del Excel
    And hace clic en Save
    Then debería ver el perfil del empleado creado
    And se captura screenshot con timestamp

    Examples:
      | NroFila |
      | 1       |
      | 2       |
      | 3       |
