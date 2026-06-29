Feature: Gestión de Empleados (PIM)

  Scenario: 4. Navegar a la sección PIM
    Given el usuario ha iniciado sesión correctamente
    When hace clic en el menú PIM
    Then debería ver la página de PIM

  Scenario: 5. Agregar nuevo empleado en PIM
    Given el usuario está en la sección PIM
    When hace clic en botón Add
    And ingresa nombre "Juan" y apellido "Perez"
    And hace clic en Save
    Then debería ver el perfil del empleado creado

  Scenario: 6. Buscar empleado existente
    Given el usuario está en la sección PIM
    When ingresa un nombre de empleado en el campo de búsqueda
    And hace clic en el botón Search
    Then debería ver los resultados de búsqueda
