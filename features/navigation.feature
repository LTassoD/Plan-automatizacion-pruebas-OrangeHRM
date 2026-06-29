Feature: Navegación de Módulos Principales

  Scenario: 7. Navegar a la sección Leave
    Given el usuario ha iniciado sesión correctamente
    When hace clic en el menú Leave
    Then debería ver la página de Leave

  Scenario: 8. Navegar a la sección Admin
    Given el usuario ha iniciado sesión correctamente
    When hace clic en el menú Admin
    Then debería ver la página de Admin

  Scenario: 9. Verificar menú My Info
    Given el usuario ha iniciado sesión correctamente
    When hace clic en el menú My Info
    Then debería ver su información personal
