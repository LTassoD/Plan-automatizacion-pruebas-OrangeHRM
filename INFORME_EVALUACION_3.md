# INFORME DE EVIDENCIAS
## EVALUACIÓN PARCIAL 3: ANALIZANDO LOS RESULTADOS OBTENIDOS

**Software bajo prueba:** OrangeHRM (opensource-demo.orangehrmlive.com — Admin / admin123)
**Framework:** Behave 1.2.6 + Selenium WebDriver 4.28 + Python 3.14
**Enfoque:** Data-Driven Testing con Excel (openpyxl)
**Navegador:** Google Chrome 149 (headless / visual según variable HEADLESS)

---

**Integrantes:**
- Estudiante: Tasso, Luis — Sección: 802V
- Profesor: Manuel Soto
- Asignatura: API0101 — Automatización de Pruebas

---

## III. Análisis y Evaluación de los Resultados de las Pruebas Automatizadas

---

### 1. EJECUCIÓN DE PRUEBAS Y REGISTRO DE EVIDENCIAS (E1)

#### 1.1 Verificación del ambiente antes de ejecutar

| Requisito | Estado | Evidencia |
|-----------|--------|-----------|
| ChromeDriver compatible con Chrome 149 | ✅ | Ejecución sin errores de versión |
| Acceso a OrangeHRM (Admin/admin123) | ✅ | Login exitoso en los 29 escenarios |
| Proyecto compila sin errores | ✅ | `python -m behave` sin errores de importación |
| Datos residuales limpios | ✅ | `testData/*.xlsx` generados fresh con `generar_excel.py` |
| Reporte JSON generado post-ejecución | ✅ | `reporte.json` con 10 features, 29 escenarios |

#### 1.2 Plan de pruebas ejecutado — 29 escenarios, 10 features

| Feature | Archivo | Casos | Tipo | Escenarios | Resultado |
|---------|---------|-------|------|------------|-----------|
| Login y Validación | `login.feature` | 1, 2, 4, 10 | Funcional + Assert fallido | 4 | 3 PASS · 1 FAIL (intencional) |
| Gestión de Sesión | `sesion_management.feature` | 3 | Logout | 1 | 1 PASS |
| Navegación | `navigation.feature` | 7, 8, 9 | Navegación entre módulos | 3 | 3 PASS |
| PIM Management | `pim_management.feature` | 11 | CRUD básico | 3 | 3 PASS |
| Empleados | `empleados.feature` | 5 | Data-Driven (3 filas Excel) | 3 | 3 PASS |
| Búsqueda | `busqueda.feature` | 6 | Data-Driven con filtros | 3 | 3 PASS |
| Edición | `edicion.feature` | 7 | Data-Driven | 3 | 3 PASS |
| Eliminación | `eliminacion.feature` | 8 | Data-Driven | 3 | 3 PASS |
| Perfil My Info | `perfil.feature` | 13 | Data-Driven | 3 | 3 PASS |
| Licencias | `licencias.feature` | 14 | Data-Driven | 3 | 3 PASS |

#### 1.3 Evidencias generadas

- **133 screenshots** en `evidencias/` con formato `screenshot_AAAAMMDD_HHMMSS.png` (timestamp permite orden cronológico)
- **Reporte HTML** (`reporte.html`) con tabla de resultados por feature, estado y duración
- **Reporte JSON** (`reporte.json`) con estructura completa de behave (features → scenarios → steps con duración en nanosegundos)

#### 1.4 TC_004: Documentación del fallo intencional

| Aspecto | Detalle |
|---------|---------|
| **Escenario** | Caso 4: "Assert falla en verificación de título" (`login.feature:18`) |
| **Step que falla** | `Then el título debe ser "OrangeHRM OS 5.7"` (`orangehrm_steps.py:248`) |
| **Valor esperado** | `"OrangeHRM OS 5.7"` |
| **Valor real** | `"OrangeHRM"` |
| **Causa del fallo** | El título real del dashboard es "OrangeHRM", no incluye la versión "OS 5.7". El assert fue diseñado intencionalmente para fallar. |
| **Propósito** | Demostrar que el hook `@after_scenario` en `environment.py:22` captura automáticamente un screenshot cuando un escenario falla. Esto verifica que el mecanismo de evidencia en fallos funciona correctamente. |
| **Evidencia** | `evidencias/screenshot_20260616_*.png` — captura automática del momento exacto del fallo. |

---

### 2. EVALUACIÓN DE RESULTADOS DE LAS PRUEBAS, PARA APORTAR AL CICLO DE VIDA DEL SOFTWARE (E2)

#### 2.1 Análisis de resultados por módulo

**Login y Autenticación (3/4 PASS):**
- TC_001 (login exitoso): La URL contiene "dashboard" tras ingresar credenciales válidas. Tiempo: ~3s.
- TC_002 (credenciales inválidas): El mensaje `.oxd-alert-content` se muestra correctamente. Tiempo: ~2s.
- TC_004 (assert título): **FALLA INTENCIONAL** — documentado en sección 1.4.
- TC_010 (campos vacíos): Los mensajes de validación aparecen en ambos campos. Tiempo: ~2s.

**Navegación y Sesión (4/4 PASS):**
- TC_003 (logout): El flujo dropdown de usuario → Logout → URL auth/login funciona correctamente.
- TC_007/008/009 (Leave, Admin, My Info): La navegación por menú lateral carga las URLs esperadas.

**PIM CRUD (12/12 PASS, Data-Driven 3 filas cada uno):**
- TC_005 (Registro): Lectura desde `dataEmpleados.xlsx`, creación con login details toggle.
- TC_006 (Búsqueda): Filtros por nombre y Employee ID desde `dataFiltros.xlsx`.
- TC_007_edicion (Edición): Actualización de Job Title y Subunit desde `dataEdicion.xlsx`.
- TC_008 (Eliminación): Flujo completo seleccionar → Delete Selected → Yes, Delete.

**Perfil y Licencias (6/6 PASS, Data-Driven 3 filas cada uno):**
- TC_013 (My Info): Carga correcta de `viewPersonalDetails`.
- TC_014 (Leave Apply): Carga correcta de sección Leave con tab Apply.

#### 2.2 Aporte al ciclo de vida del software

1. **Detección temprana de regresiones:** Si OrangeHRM modifica su UI, la suite falla inmediatamente, alertando al equipo antes de impactar a usuarios.
2. **Documentación ejecutable:** Los 10 archivos `.feature` describen el comportamiento esperado en lenguaje Gherkin legible por stakeholders no técnicos.
3. **Base para CI/CD:** La suite puede integrarse en GitHub Actions para ejecución automatizada post-deploy.
4. **Cobertura Data-Driven:** 18 de 29 escenarios (62%) usan datos externos desde Excel, permitiendo expandir cobertura sin modificar código.

---

### 3. ANÁLISIS E IDENTIFICACIÓN DEL ORIGEN DE LAS INCIDENCIAS — OPORTUNIDADES DE MEJORA (E1)

Cada oportunidad sigue la estructura: **A)** Observación desde el resultado, **B)** Causa técnica identificada, **C)** Acción concreta propuesta.

---

#### Oportunidad 1: Internacionalización del menú lateral

**A) Observación desde el resultado:**
Durante la ejecución, los TC_007, TC_008 y TC_009 (navegación) fallaron porque el menú lateral mostraba texto en chino. El reporte `reporte.json` muestra `AssertionError: Menu 'Leave' no encontrado` para estos 3 escenarios.

**B) Causa técnica identificada:**
El servidor demo de OrangeHRM cambia su locale según configuración regional. Los elementos `span.oxd-main-menu-item--name` contienen "休假" (Leave), "管理员" (Admin) y "个人信息管理系统" (PIM) en vez de los textos en inglés esperados por `_click_menu()`.

**C) Acción concreta propuesta (ya implementada):**
Se creó `MENU_TRANSLATIONS` (`orangehrm_steps.py:7-20`) que mapea cada nombre de menú inglés a sus variantes en chino. `_click_menu()` ahora prueba ambas variantes antes de fallar. Esto hace la suite resistente al locale del servidor.

---

#### Oportunidad 2: Validación de título vs URL

**A) Observación desde el resultado:**
TC_004 falla porque el assert de título espera "OrangeHRM OS 5.7" pero recibe "OrangeHRM". El reporte `reporte.json` en `login.feature:18` muestra `Assertion Failed: Título esperado: 'OrangeHRM OS 5.7', actual: 'OrangeHRM'`.

**B) Causa técnica identificada:**
El step `el título debe ser "{expected_title}"` (`orangehrm_steps.py:248`) usa `driver.title` que retorna solo "OrangeHRM". La versión del producto no está incluida en el título de la página HTML.

**C) Acción concreta propuesta:**
Reemplazar la validación por título con validación por URL: `assert "dashboard" in driver.current_url`, que es más estable y no depende del texto visible. Este cambio ya se aplicó en `step_verify_dashboard()`.

---

#### Oportunidad 3: Robustez del botón Save ante spinners

**A) Observación desde el resultado:**
En TC_005 (registro de empleados), el botón Save ocasionalmente no respondía al click. El log de Selenium mostraba `element click intercepted` porque el spinner `.oxd-loading-spinner` bloqueaba el botón.

**B) Causa técnica identificada:**
OrangeHRM usa el framework OX que muestra un spinner de carga mientras procesa. El spinner tapa el botón `button[type='submit']` intermitentemente, y `element_to_be_clickable` no siempre es suficiente.

**C) Acción concreta propuesta (ya implementada):**
Se implementó un fallback con `execute_script("arguments[0].click();", btn)` en `step_click_save()` (`orangehrm_steps.py:127-133`) y se agregó `_wait_spinner_done()` (`data_driven_steps.py:40-46`) que espera a que el spinner desaparezca antes de interactuar.

---

#### Oportunidad 4: Tiempo de ejecución de la suite completa

**A) Observación desde el resultado:**
La suite completa de 29 escenarios toma aproximadamente 7 minutos. Los escenarios PIM son los más lentos (~40s cada uno) debido a navegación + espera de carga de tabla.

**B) Causa técnica identificada:**
Cada escenario abre una nueva sesión de Chrome (driver nueva), navega a OrangeHRM y hace login. Esto suma ~10-15s de overhead por escenario solo en configuración.

**C) Acción concreta propuesta:**
Implementar ejecución paralela con `behave -j 4` (4 workers) para reducir el tiempo total de ~7 min a ~2 min. Esto requiere asegurar que los escenarios no compartan estado (ya es el caso, cada uno tiene su propio driver).

---

#### Oportunidad 5: Trazabilidad de datos Data-Driven

**A) Observación desde el resultado:**
Los 6 archivos Excel en `testData/` contienen los datos de prueba, pero no hay un mecanismo que garantice que los datos en el Excel corresponden a la ejecución actual.

**B) Causa técnica identificada:**
Los archivos Excel se generan con `generar_excel.py` pero pueden ser modificados manualmente entre ejecuciones, perdiendo trazabilidad.

**C) Acción concreta propuesta:**
Versionar los archivos Excel en el repositorio Git y regenerarlos con `generar_excel.py` antes de cada ejecución como paso pre-commit hook. Esto asegura que los datos de prueba son siempre los mismos.

---

### 4. GENERACIÓN DE MÉTRICAS DE CALIDAD (E2)

#### 4.1 Métricas PPT 3.3.1 con origen verificable

Cada métrica se vincula a su fuente exacta en los artefactos generados en esta ejecución.

| Métrica | Fórmula | Resultado | Fuente en el reporte |
|---------|---------|-----------|----------------------|
| **% Automatizable** | (Casos automatizados / Casos totales) × 100 | **100%** (29/29) | `reporte.html` — Resumen Final: 29 escenarios ejecutados de 29 planificados |
| **Progreso de Automatización** | (Escenarios ejecutados / Planificados) × 100 | **100%** (29/29) | `reporte.json` — 10 features × 29 scenarios total |
| **Productividad de Diseño** | Escenarios / Horas de diseño | **7.25 escenarios/hora** (29 / 4 hrs) | Tiempo asignado: 4 hrs (evaluación) |
| **Productividad de Ejecución** | Escenarios / Tiempo total | **0.067 escenarios/s** (29 / ~435s) | `reporte.json` — suma de duraciones individuales |
| **Tasa de Fallos** | (Fallos / Total) × 100 | **3.45%** (1/29) | `reporte.html` — 28 PASS · 1 FAIL. El único fallo es TC_004 (intencional, documentado en sección 1.4) |

#### 4.2 Interpretación de métricas

- **100% automatizable:** Todos los casos de prueba del plan pudieron ser implementados con Behave + Selenium. No hubo casos que requirieran intervención manual.
- **Progreso del 100%:** La ejecución cubrió la totalidad de los 29 escenarios diseñados, sin omisiones.
- **Productividad de diseño (7.25 esc/hora):** En las 4 horas asignadas se diseñaron e implementaron 29 escenarios, lo que indica una curva de aprendizaje eficiente del framework.
- **Tasa de fallos del 3.45%:** Corresponde únicamente a TC_004, diseñado intencionalmente para fallar. Si se excluye, la tasa es 0%. Esto demuestra que la suite es estable.
- **Cobertura funcional:** 7 módulos de OrangeHRM cubiertos (Login, Dashboard, PIM, Leave, Admin, My Info, Recruitment navegación).

---

### 5. PROPUESTA DE MEJORA PARA LAS INCIDENCIAS Y RIESGOS IDENTIFICADOS (E1 y E2)

Cada propuesta sigue la estructura: **Dato → Causa → Acción → Impacto**.

---

#### Mejora 1 — Al producto (OrangeHRM): Mensajes de error diferenciados

| Elemento | Detalle |
|----------|---------|
| **Dato** | TC_002 (`login.feature:11`) muestra que el mensaje de error para usuario inválido es genérico: "Invalid credentials". El step `step_verify_error()` valida solo que el alert sea visible, no su contenido específico. |
| **Causa** | OrangeHRM devuelve el mismo texto "Invalid credentials" tanto para usuario inexistente como para contraseña incorrecta. Esto impide al usuario saber qué campo corrigió mal. |
| **Acción** | Agregar un nuevo escenario TC_002b que distinga ambos casos. Si OrangeHRM implementara mensajes diferenciados (ej: "Usuario no encontrado" vs "Contraseña incorrecta"), el test debería validarlos por separado. |
| **Impacto** | Mejora la usabilidad del producto y la seguridad informativa. Afecta al ciclo de vida en la fase de mantenimiento evolutivo. |

---

#### Mejora 2 — Al producto (OrangeHRM): Localización consistente

| Elemento | Detalle |
|----------|---------|
| **Dato** | Durante la ejecución, el menú lateral apareció en chino (INC-01, INC-02). Los elementos `span.oxd-main-menu-item--name` mostraban caracteres chinos. |
| **Causa** | OrangeHRM aplica locale según configuración del servidor sin persitencia de preferencia del usuario. Un usuario que configura inglés puede encontrar el menú en otro idioma al recargar. |
| **Acción** | Agregar un selector de idioma persistente en la UI (cookie o preferencia de usuario) para que el locale elegido se mantenga entre sesiones. |
| **Impacto** | Mejora la experiencia de usuario internacional. Afecta al ciclo de vida en la fase de mantenimiento y evolución de UI. |

---

#### Mejora 3 — Al proceso (Framework): Page Object Model

| Elemento | Detalle |
|----------|---------|
| **Dato** | En `orangehrm_steps.py` y `data_driven_steps.py`, los selectores CSS/XPath están dispersos dentro de las funciones step. Por ejemplo, el selector `span.oxd-main-menu-item--name` aparece en 2 archivos distintos. Si OrangeHRM cambiara esta clase, habría que modificar 2 archivos. |
| **Causa** | El framework actual usa step definitions planas sin separación de capas. La lógica de localización (cómo encontrar un elemento) está mezclada con la lógica de negocio (qué hacer con él). |
| **Acción** | Refactorizar implementando Page Object classes: `LoginPage`, `PimPage`, `LeavePage`, etc. Cada clase encapsula los selectores y métodos de interacción de una página. Los steps solo llaman a métodos de Page Objects. |
| **Impacto** | Un cambio de selector requiere modificar 1 archivo (el Page Object) en vez de N steps. Mantenibilidad centralizada. Afecta al ciclo de vida en la fase de mantenimiento del framework de pruebas. |

---

#### Mejora 4 — Al proceso (Framework): Ejecución paralela

| Elemento | Detalle |
|----------|---------|
| **Dato** | La suite completa toma ~7 minutos (reporte: duración total ~435s). Cada escenario nuevo aumenta ~15s de overhead por apertura de Chrome + login. |
| **Causa** | Los escenarios se ejecutan secuencialmente y cada uno crea su propia instancia de WebDriver (`environment.py:15`). No hay reutilización de sesión ni paralelismo. |
| **Acción** | Configurar `behave -j 4` (paralelización con 4 workers). Los escenarios son independientes (no comparten estado), por lo que la paralelización es segura. |
| **Impacto** | Reduce el tiempo total de ~7 min a ~2 min. Permite ejecutar la suite en pipelines CI/CD sin afectar el tiempo de deploy. Afecta al ciclo de vida en la fase de integración continua. |

---

#### Mejora 5 — Al proceso (Framework): Logging estructurado

| Elemento | Detalle |
|----------|---------|
| **Dato** | Actualmente la suite usa `print()` comentado (`orangehrm_steps.py:60`) y asserts sin logs. Cuando un escenario falla, solo se obtiene el traceback de Python. |
| **Causa** | No hay un sistema de logging que registre el flujo de ejecución (timestamp, nivel, mensaje). La depuración de fallos intermitentes requiere re-ejecutar con `print` agregados manualmente. |
| **Acción** | Implementar el módulo estándar `logging` de Python con formato `[YYYY-MM-DD HH:MM:SS] [LEVEL] mensaje`. Agregar logs informativos en cada step (ej: "Login exitoso en 2.3s") y de error cuando falle un assert. |
| **Impacto** | Los fallos intermitentes se diagnostican más rápido. Los logs estructurados pueden integrarse con herramientas de monitoreo (Splunk, ELK). Afecta al ciclo de vida en las fases de pruebas y operaciones. |

---

#### Mejora 6 — Al producto + proceso: CI/CD con GitHub Actions

| Elemento | Detalle |
|----------|---------|
| **Dato** | La suite se ejecuta manualmente desde terminal o PyCharm. No hay ejecución automática programada ni por evento. |
| **Causa** | No hay pipeline configurado. El proyecto no tiene archivo `.github/workflows/` para CI/CD. |
| **Acción** | Crear workflow de GitHub Actions que ejecute `behave features/` con `HEADLESS=1` en cada push a `main` y generar reporte HTML como artefacto descargable. |
| **Impacto** | Las regresiones se detectan automáticamente en cada commit, sin intervención manual. Afecta al ciclo de vida en las fases de integración y despliegue. |

---

### 6. REFLEXIONES Y CONCLUSIONES INDIVIDUALES DEL PROCESO

**Estudiante 1: Luis Tasso**

**Dificultades encontradas:**
- **Inestabilidad del ambiente demo:** OrangeHRM cambió su locale a chino durante el desarrollo, lo que rompió todos los localizadores del menú lateral. Esto me obligó a diseñar un sistema de traducción dinámica con `MENU_TRANSLATIONS`, lo que a su vez me enseñó a no confiar en texto visible como selector único.
- **Tiempos de carga variables:** El sitio demo muestra tiempos de respuesta que varían entre 2s y 30s. Aprendí a combinar `WebDriverWait` (para condiciones) con `time.sleep()` (para pausas cortas predecibles) en lugar de depender solo de uno.
- **Manejo de encoding en behave:** Al agregar comentarios al código, accidentalmente quité las tildes de los decoradores de steps, lo que hizo que behave no encontrara las definiciones. Esto me enseñó que behave compara el texto del feature file con el decorador caractér por carácter, incluyendo acentos.

**Aprendizajes clave:**
1. Un fallo bien documentado vale más que 10 pasos sin explicación.
2. La trazabilidad de métricas (cada número debe poder señalarse en su fuente) es lo que distingue un informe básico de uno profesional.
3. El Page Object Model no es opcional cuando el framework escala más allá de 3 features.

**Proyecciones:**
- Implementar GitHub Actions para que la suite se ejecute automáticamente en cada commit.
- Migrar los steps actuales a Page Object classes para mejorar mantenibilidad.
- Agregar Allure Reports para visualización de tendencias históricas.

---

### 7. REFLEXIONES Y CONCLUSIÓN GRUPAL SOBRE EL PROCESO

**Roles asumidos:**
- **E1 (Luis Tasso):** Arquitectura de automatización, implementación de steps genéricos y Data-Driven, manejo de Excel, generación de reportes HTML/PPT, análisis de resultados, métricas de calidad, propuestas de mejora, y documentación del informe.

**Evaluación del framework vs. evaluación del producto:**

| Dimensión | Mejoras al producto (OrangeHRM) | Mejoras al proceso (Framework) |
|-----------|-------------------------------|-------------------------------|
| ¿Qué se evalúa? | Funcionalidades del SUT | Mantenibilidad y escalabilidad del código de pruebas |
| Ejemplos | Mensajes de error diferenciados, localización persistente | Page Object Model, logging estructurado, paralelización |
| Impacto en ciclo de vida | Fases de mantenimiento evolutivo y UX | Fases de integración continua y operaciones |

**Calidad del entregable:**
- **29/29 escenarios ejecutados** — cobertura completa del plan
- **96.55% aprobación** — único fallo es intencional y documentado
- **133 evidencias visuales** — trazabilidad completa de cada paso
- **6 archivos Excel** — Data-Driven funcional con datos versionables
- **Reporte HTML** — métricas trazables con origen verificable
- **Código comentado** — cada función documentada en español

**Conclusión final:**
La automatización de pruebas para OrangeHRM cumple con los objetivos de la evaluación parcial 3: se ejecutaron los 29 escenarios de forma exhaustiva, se registraron las evidencias (screenshots, reportes), se identificaron oportunidades de mejora con estructura A+B+C, se generaron métricas trazables al reporte, y se propusieron mejoras con dato→causa→acción→impacto tanto para el producto como para el proceso. La suite está lista para integrarse en un pipeline CI/CD y servir como herramienta de regresión continua.
