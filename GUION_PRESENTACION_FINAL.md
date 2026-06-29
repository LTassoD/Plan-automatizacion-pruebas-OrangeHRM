# Guion de Presentación — Evaluación Final Transversal
**Duración:** ~10 minutos | **Estudiante:** Luis Tasso | **Sección:** 802V

---

### Slide 1 — Portada *(20s)*

> "Buenos días profesor Manuel Soto. Soy Luis Tasso de la sección 802V y presento la Evaluación Final Transversal de Automatización de Pruebas. El software bajo prueba es OrangeHRM, automatizado con Behave, Selenium WebDriver y Python."

---

### Slide 2 — Agenda *(30s)*

> "La presentación cubre seis bloques: primero el plan de pruebas automatizadas con su cronograma por sprint, luego la implementación mostrando trazabilidad y codificación, después los resultados de ejecución con métricas de calidad, las oportunidades de mejora detectadas, las propuestas formales para producto y proceso, y finalmente las conclusiones y proyecciones."

---

### Slide 3 — Plan de Pruebas y Cronograma *(1 min 30s)*

> "Comenzamos con el plan de pruebas. El caso seleccionado es OrangeHRM, un sistema de gestión de recursos humanos open source. Evaluamos 7 módulos: Login, Dashboard, PIM, Leave, Admin, My Info y Sesión."

> "La automatización se planificó en 3 sprints, alineados con las evaluaciones parciales del semestre."

> **Sprint 1 — Fundamentos:** Configuración del entorno Python + Behave + Selenium, creación de features de login y sesión, implementación de steps genéricos y el hook de captura de screenshots. Entregamos 4 escenarios funcionando, incluyendo el fallo intencional TC_004."

> **Sprint 2 — PIM CRUD y Data-Driven:** Implementamos la lectura de datos desde Excel con openpyxl, creamos 6 features Data-Driven para el módulo PIM (registro, búsqueda, edición, eliminación de empleados). Cada caso se multiplica por 3 filas de datos."

> **Sprint 3 — Perfil, Licencias y Reportes:** Agregamos los módulos de My Info y Leave, completamos los 29 escenarios, y generamos los reportes HTML y JSON con métricas trazables."

---

### Slide 4 — Trazabilidad y Codificación *(1 min 30s)*

> "Acá está la matriz de trazabilidad completa. 11 requisitos del curso mapeados a sus funcionalidades, escenarios Gherkin y resultados. 10 PASS, 1 FAIL intencional."

> "La codificación sigue el enfoque BDD con Gherkin. Por ejemplo, el escenario de login exitoso se lee en lenguaje natural."

*(Señalar la tabla)*

> "RF03 a RF06 — el CRUD de PIM completo — está implementado con Data-Driven. Cada escenario en Gherkin usa Scenario Outline con Examples que referencian filas de Excel. El mismo step se ejecuta con 3 conjuntos de datos diferentes."

> "Las condiciones de aceptación están definidas en cada Then. Para login exitoso: la URL debe contener 'dashboard'. Para login inválido: el mensaje de alerta debe ser visible. Para logout: la URL debe contener 'auth/login'. Para el fallo intencional: el título debe ser 'OrangeHRM OS 5.7' — y falla porque el real es 'OrangeHRM'."

---

### Slide 5 — Resultados de Ejecución *(1 min 30s)*

> "Ejecutamos 29 escenarios con 96.55% de aprobación. El único fallo es el TC_004 intencional, documentado y esperado."

*(Señalar módulos)*

> "Login: 3 de 4 PASS (el fallo es el intencional). Navegación y Sesión: 100%. PIM CRUD: 12 de 12 incluyendo los 4 casos Data-Driven con 3 filas cada uno. Perfil y Licencias: 6 de 6."

> "18 de 29 escenarios —el 62%— son Data-Driven, lo que demuestra la escalabilidad del framework."

> "Capturamos 177 screenshots como evidencia. Cada escenario genera múltiples screenshots con timestamp. Cuando un escenario falla, el hook `@after_scenario` en `environment.py` captura automáticamente el momento exacto del fallo."

---

### Slide 6 — Métricas de Calidad y Rendimiento *(1 min 30s)*

> "Presento las métricas agrupadas en dos categorías."

> **Métricas de calidad del proceso (PPT 3.3.1):**
> - 100% automatizable: todos los casos se implementaron.
> - 100% de progreso: los 29 escenarios planificados se ejecutaron.
> - Productividad de diseño: 7.25 escenarios por hora.
> - Tasa de fallos: 3.45%, que corresponde únicamente al TC_004 intencional. Si lo excluimos, la tasa es 0%.

> **Métricas de rendimiento:**
> - Tiempo promedio por escenario: 15 segundos.
> - Feature más lenta: PIM, con aproximadamente 40 segundos por escenario por las tablas de carga.
> - Overhead de setup: 25% del tiempo total se gasta en abrir el navegador y hacer login para cada escenario.
> - Cobertura Data-Driven: 62%.
> - La suite completa toma ~7 minutos en ejecución secuencial.

> "Cada métrica tiene su fuente verificable en `reporte.json` o `reporte.html`."

---

### Slide 7 — Oportunidades de Mejora *(1 min 30s)*

> "Identificamos 5 oportunidades durante el desarrollo, cada una con estructura A+B+C."

*(Señalar O1)*

> **O1 — Menú en chino.** El servidor demo cambió el locale a chino. Los escenarios de navegación fallaban porque buscaban 'Leave' pero el DOM mostraba '休假'. **Solución:** implementamos `MENU_TRANSLATIONS`, un diccionario inglés-chino para cada opción del menú."

> **O2 — Botón Save interceptado.** El spinner de OX tapaba el botón Save. **Solución:** función `_wait_spinner_done()` más fallback con JavaScript click."

> **O3 — Validación por título frágil.** TC_004 usa `driver.title` que varía según configuración. **Solución:** migramos a validación por URL con `url_contains('dashboard')`, que es más estable."

> **O4 — Tiempo de ejecución largo.** ~7 minutos para 29 escenarios. **Propuesta:** paralelización con `behave -j 4` para reducir a ~2 minutos."

> **O5 — Datos Excel no versionables.** Los archivos `.xlsx` son binarios, sin diff en git. **Propuesta:** regenerar con `generar_excel.py` antes de cada ejecución."

---

### Slide 8 — Propuestas de Mejora *(1 min)*

> "Presentamos 6 propuestas formales, divididas en producto y proceso."

> **Producto — OrangeHRM (Criterio 3):**
> **MP-01:** Mensajes de error diferenciados. Hoy 'Invalid credentials' es el mismo para usuario inexistente y contraseña incorrecta. **MP-02:** Selector de idioma persistente con cookie, para evitar el cambio de locale entre sesiones.

> **Proceso — Framework (Criterio 4):**
> **MP-03:** Page Object Model. Refactorizar los steps actuales en clases LoginPage, PimPage, LeavePage para centralizar selectores. **MP-04:** Ejecución paralela con 4 workers para reducir el tiempo de suite de 7 a 2 minutos. **MP-05:** Logging estructurado con timestamps y niveles, reemplazando los print() actuales. **MP-06:** CI/CD con GitHub Actions para ejecución automática en cada push.

> "Cada propuesta tiene impacto cuantificable: mantenibilidad, reducción de tiempo, mejor diagnóstico."

---

### Slide 9 — Stack Tecnológico: Behave + Python + Selenium *(1 min)*

> "Nuestro stack está compuesto por Python 3.14 como lenguaje base, Behave 1.2.6 como framework BDD, Selenium WebDriver 4.28 para automatización del navegador, openpyxl para lectura de Excel, y PyCharm como IDE."

> "Behave funciona de forma similar a Cucumber para Java: los archivos `.feature` contienen los escenarios en Gherkin, y los steps se definen en archivos Python con decoradores `@given`, `@when`, `@then`. La configuración del driver se maneja en `environment.py` con hooks `before_scenario` y `after_scenario`."

> "Para ejecutar: `python -m behave features/` ejecuta toda la suite. `--format json -o reporte.json` genera el reporte estructurado. La variable de entorno `HEADLESS=0` permite ver el navegador durante la ejecución para depuración."

> "El ciclo de vida del proyecto se gestiona con Git para control de versiones y requirements.txt para dependencias."

---

### Slide 10 — Conclusiones y Cierre *(30s)*

> "En resumen: 29 escenarios ejecutados, 96.55% de aprobación, suite bilingüe inglés-chino, Data-Driven funcional con 18 escenarios parametrizados, 177 screenshots de evidencia, métricas trazables, 5 oportunidades documentadas y 6 propuestas de mejora con impacto medible."

> "La automatización está lista para integrarse en un pipeline CI/CD."

> "Muchas gracias. Quedo atento a sus preguntas."

---

## Resumen de Tiempos

| Slide | Tema | Duración |
|-------|------|----------|
| 1 | Portada | 20s |
| 2 | Agenda | 30s |
| 3 | Plan de Pruebas y Cronograma | 1min 30s |
| 4 | Trazabilidad y Codificación | 1min 30s |
| 5 | Resultados de Ejecución | 1min 30s |
| 6 | Métricas de Calidad y Rendimiento | 1min 30s |
| 7 | Oportunidades de Mejora | 1min 30s |
| 8 | Propuestas de Mejora | 1min |
| 9 | Stack Tecnológico | 1min |
| 10 | Conclusiones y Cierre | 30s |
| **Total** | | **~10 min** |
