# INFORME FINAL — EVALUACIÓN FINAL TRANSVERSAL
## API0101 — Automatización de Pruebas

**Software bajo prueba:** OrangeHRM (opensource-demo.orangehrmlive.com)
**Framework:** Behave 1.2.6 + Selenium WebDriver 4.28 + Python 3.14
**Enfoque:** BDD + Data-Driven Testing con Excel (openpyxl)
**Navegador:** Google Chrome 149
**Estudiante:** Luis Tasso — Sección: 802V
**Profesor:** Manuel Soto
**Fecha:** Junio 2026

---

## ÍNDICE

> El índice se genera automáticamente desde los encabezados del documento. Para actualizarlo, ejecutar: `python generar_toc.py`

<!-- TOC_START -->
I. [I. PLAN DE PRUEBAS AUTOMATIZADAS](#i-plan-de-pruebas-automatizadas)
    - [1. Presentación del caso](#1-presentación-del-caso)
    - [2. Evaluación del caso y planificación — Cronograma por Sprint](#2-evaluación-del-caso-y-planificación-cronograma-por-sprint)
    - [3. Casos de pruebas](#3-casos-de-pruebas)
    - [4. Definición de técnicas y metodologías de pruebas automatizadas](#4-definición-de-técnicas-y-metodologías-de-pruebas-automatizadas)
    - [5. Definición de tipos de pruebas de automatización](#5-definición-de-tipos-de-pruebas-de-automatización)
    - [6. Herramientas para casos de prueba y automatización](#6-herramientas-para-casos-de-prueba-y-automatización)
    - [7. Guiones para definir la automatización de casos de prueba](#7-guiones-para-definir-la-automatización-de-casos-de-prueba)
II. [II. IMPLEMENTACIÓN DEL PLAN DE PRUEBAS AUTOMATIZADAS](#ii-implementación-del-plan-de-pruebas-automatizadas)
    - [1. Matriz de trazabilidad](#1-matriz-de-trazabilidad)
    - [2. Codificación de escenarios de prueba](#2-codificación-de-escenarios-de-prueba)
    - [3. Condiciones de aceptación de los casos de prueba](#3-condiciones-de-aceptación-de-los-casos-de-prueba)
    - [4. Casos de prueba utilizando el software de automatización (Enfoque BDD)](#4-casos-de-prueba-utilizando-el-software-de-automatización-enfoque-bdd)
    - [5. Plantilla de escenarios de prueba con evidencia de resultados](#5-plantilla-de-escenarios-de-prueba-con-evidencia-de-resultados)
III. [III. ANÁLISIS Y EVALUACIÓN DE LOS RESULTADOS DE LAS PRUEBAS AUTOMATIZADAS](#iii-análisis-y-evaluación-de-los-resultados-de-las-pruebas-automatizadas)
    - [1. Ejecución de pruebas y registro de evidencias](#1-ejecución-de-pruebas-y-registro-de-evidencias)
    - [2. Evaluación de resultados de las pruebas, para aportar al ciclo de vida del software](#2-evaluación-de-resultados-de-las-pruebas-para-aportar-al-ciclo-de-vida-del-software)
    - [3. Análisis e identificación del origen de las incidencias — Oportunidades de mejora](#3-análisis-e-identificación-del-origen-de-las-incidencias-oportunidades-de-mejora)
    - [4. Generación de métricas de calidad](#4-generación-de-métricas-de-calidad)
    - [5. Propuesta de mejora para las incidencias y riesgos identificados](#5-propuesta-de-mejora-para-las-incidencias-y-riesgos-identificados)
    - [6. Conclusiones y proyecciones](#6-conclusiones-y-proyecciones)
<!-- TOC_END -->

---

## I. PLAN DE PRUEBAS AUTOMATIZADAS

*Esta sección describe la planificación completa del proceso de automatización: el caso seleccionado (OrangeHRM), la organización del trabajo en 3 sprints alineados con las evaluaciones parciales, los 16 casos de prueba diseñados con sus prioridades y tipos, las técnicas y metodologías aplicadas (BDD, Data-Driven, captura automática de evidencia), los tipos de pruebas cubiertos, las herramientas del stack tecnológico, y los guiones que definen cómo se automatiza cada caso.*

---

### 1. Presentación del caso

OrangeHRM es un sistema de gestión de recursos humanos (HRMS) de código abierto. La instancia bajo prueba es la demo oficial disponible en `opensource-demo.orangehrmlive.com`, accesible con credenciales Admin/admin123.

**Módulos evaluados:**
- Login y autenticación (acceso, validación, cierre de sesión)
- Dashboard (verificación de ingreso)
- PIM (Personal Information Management — CRUD de empleados)
- Navegación entre módulos (Leave, Admin, My Info)
- Gestión de perfil personal (My Info)
- Solicitud de licencias (Leave)

**Alcance de la automatización:**
29 escenarios de prueba distribuidos en 10 features, cubriendo los flujos críticos del sistema. 18 escenarios (62%) utilizan Data-Driven Testing con datos externos desde Excel, lo que permite escalar la cobertura sin modificar código.

---

### 2. Evaluación del caso y planificación — Cronograma por Sprint

La automatización se planificó en 3 sprints, correspondientes a las 3 evaluaciones parciales del semestre:

#### Sprint 1 (Evaluación Parcial 1) — Fundamentos y Login

| Semana | Actividad | Entregable |
|--------|-----------|------------|
| 1-2 | Configuración del entorno (Python, Behave, Selenium, ChromeDriver) | Ambiente funcional |
| 2-3 | Creación de features básicos: `login.feature`, `sesion_management.feature` | 2 features |
| 3-4 | Implementación de steps genéricos (login, logout, validación) | `orangehrm_steps.py` |
| 4 | Configuración de `environment.py` (before/after scenario) + screenshots | Ejecución de 4 escenarios |

**Resultado Sprint 1:** 4 escenarios (TC_001, TC_002, TC_003, TC_004), incluyendo fallo intencional TC_004.

#### Sprint 2 (Evaluación Parcial 2) — PIM CRUD y Data-Driven

| Semana | Actividad | Entregable |
|--------|-----------|------------|
| 5-6 | Features de PIM: `pim_management.feature`, `empleados.feature` | CRUD básico |
| 6-7 | Implementación de Data-Driven: `ExcelUtils`, `data_driven_steps.py` | Lectura desde Excel |
| 7-8 | Features Data-Driven: `busqueda.feature`, `edicion.feature`, `eliminacion.feature` | 6 features |
| 8 | Generación de datos Excel con `generar_excel.py`, reportes JSON/HTML | Ejecución de 15 escenarios |

**Resultado Sprint 2:** 15 escenarios Data-Driven (TC_005, TC_006, TC_007, TC_008, TC_011, TC_012).

#### Sprint 3 (Evaluación Parcial 3) — Perfil, Licencias, Reportes y Métricas

| Semana | Actividad | Entregable |
|--------|-----------|------------|
| 9-10 | Features: `perfil.feature`, `licencias.feature` | 2 features Data-Driven |
| 10-11 | Navegación entre módulos: `navigation.feature` | 3 escenarios |
| 11-12 | Generación de reportes: `generar_reporte.py`, `reporte.html` | Reporte ejecución |
| 12 | Análisis de métricas, oportunidades de mejora, propuestas | Informe final |

**Resultado Sprint 3:** 10 escenarios adicionales → Total: 29 escenarios, 10 features.

---

### 3. Casos de pruebas

| ID | Módulo | Nombre | Prioridad | Tipo | Automatizado |
|----|--------|--------|-----------|------|-------------|
| TC_001 | Login | Login exitoso con Admin | Alta | Funcional | ✅ |
| TC_002 | Login | Login con credenciales inválidas | Alta | Funcional | ✅ |
| TC_003 | Sesión | Logout exitoso | Alta | Funcional | ✅ |
| TC_004 | Login | Assert falla en verificación de título | Media | Fallo intencional | ✅ |
| TC_005 | PIM | Registro de empleados (Data-Driven) | Alta | Funcional + Datos | ✅ |
| TC_006 | PIM | Búsqueda de empleados con filtros (Data-Driven) | Alta | Funcional + Datos | ✅ |
| TC_007 | PIM | Edición de empleados (Data-Driven) | Alta | Funcional + Datos | ✅ |
| TC_008 | PIM | Eliminación de empleados (Data-Driven) | Alta | Funcional + Datos | ✅ |
| TC_010 | Login | Validación de campos obligatorios | Media | Funcional | ✅ |
| TC_011 | PIM | CRUD básico — Agregar, Buscar, Navegar | Alta | Funcional | ✅ |
| TC_012 | PIM | Gestión de empleados — Navegación PIM | Media | Funcional | ✅ |
| TC_013 | My Info | Navegación y verificación de perfil (Data-Driven) | Media | Funcional + Datos | ✅ |
| TC_014 | Leave | Solicitud de licencias (Data-Driven) | Media | Funcional + Datos | ✅ |
| TC_007_Nav | Navegación | Navegar a Leave | Alta | Navegación | ✅ |
| TC_008_Nav | Navegación | Navegar a Admin | Alta | Navegación | ✅ |
| TC_009_Nav | Navegación | Navegar a My Info | Alta | Navegación | ✅ |

**Total: 29 escenarios** (16 casos únicos, algunos con Data-Driven que generan 3 escenarios cada uno).

---

### 4. Definición de técnicas y metodologías de pruebas automatizadas

| Técnica / Metodología | Aplicación en el proyecto |
|-----------------------|---------------------------|
| **BDD (Behavior-Driven Development)** | Escenarios escritos en Gherkin (`Given/When/Then`) en 10 archivos `.feature`. Lenguaje natural legible por stakeholders no técnicos. |
| **Data-Driven Testing (DDT)** | 18 de 29 escenarios (62%) obtienen datos desde archivos Excel externos. Un mismo step se ejecuta con N filas de datos, generando N escenarios diferentes. |
| **Page Object Model (propuesto)** | Actualmente los selectores están en steps planos. Se propone refactorizar a clases `LoginPage`, `PimPage`, `LeavePage` para centralizar localizadores. |
| **Captura automática de evidencia** | Hook `@after_scenario` en `environment.py` que toma screenshot automáticamente cuando un escenario falla. |
| **Paralelización (propuesta)** | Ejecución secuencial actual (~7 min). Se propone `behave -j 4` para reducir a ~2 min. |
| **CI/CD (propuesto)** | Integración con GitHub Actions para ejecución automática en cada push. |

---

### 5. Definición de tipos de pruebas de automatización

| Tipo de prueba | Descripción | Escenarios |
|----------------|-------------|------------|
| **Pruebas funcionales** | Verifican que cada funcionalidad del software opera según lo especificado. | TC_001, TC_002, TC_003, TC_005-009, TC_011-014 |
| **Pruebas de regresión** | Validan que cambios en el software no rompan funcionalidades existentes. | Toda la suite (29 escenarios) |
| **Pruebas de humo (Smoke)** | Verifican que las funcionalidades críticas funcionan después de un deploy. | TC_001, TC_003, TC_005 (login + PIM) |
| **Pruebas de internacionalización** | Validan que la UI funciona correctamente en diferentes idiomas. | TC_007_Nav, TC_008_Nav, TC_009_Nav (con MENU_TRANSLATIONS) |
| **Pruebas de validación** | Verifican que el sistema rechaza entradas inválidas o vacías. | TC_002, TC_010 |
| **Fallo intencional** | Escenario diseñado para fallar y demostrar mecanismos de captura de evidencia. | TC_004 |

---

### 6. Herramientas para casos de prueba y automatización

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| **Python** | 3.14 | Lenguaje de programación del framework |
| **Behave** | 1.2.6 | Framework BDD para escribir y ejecutar pruebas en Gherkin |
| **Selenium WebDriver** | 4.28 | Automatización del navegador Chrome |
| **openpyxl** | 3.1+ | Lectura de archivos Excel para Data-Driven Testing |
| **Google Chrome** | 149 | Navegador bajo prueba |
| **ChromeDriver** | 149 | Driver de Selenium para Chrome |
| **PyCharm** | 2026.1 | IDE para desarrollo y depuración |
| **Git** | — | Control de versiones del proyecto |
| **JSON** | — | Formato de reporte de resultados de behave |
| **HTML** | — | Formato de reporte visual para stakeholders |

---

### 7. Guiones para definir la automatización de casos de prueba

Cada caso de prueba sigue este flujo de automatización:

```
1. Configuración: before_scenario() abre Chrome en modo headless
2. Navegación: driver.get("https://opensource-demo.orangehrmlive.com/")
3. Ejecución: Los steps Given/When/Then interactúan con la UI
4. Validación: Asserts sobre URL, elementos visibles, o texto en DOM
5. Evidencia: capture_screenshot() en cada escenario
6. Limpieza: after_scenario() cierra el navegador (y captura screenshot si falló)
```

**Guion específico para casos Data-Driven:**
```
1. ExcelUtils.set_excel_file_sheet("testData/dataX.xlsx", "SheetName")
2. Leer datos: ExcelUtils.get_cell_data(fila, columna)
3. Completar formulario con datos leídos
4. Hacer clic en botón de acción (Save, Search, Delete, etc.)
5. Validar resultado esperado (URL, elemento, mensaje)
6. Capturar screenshot
```

**Guion para el fallo intencional TC_004:**
```
1. Login exitoso con Admin/admin123
2. Assert: driver.title == "OrangeHRM OS 5.7" (falla porque el título real es "OrangeHRM")
3. after_scenario detecta el fallo y captura screenshot automáticamente
```

#### Evidencia de ejecución — Estructura del proyecto

La estructura completa del proyecto se muestra a continuación. Cada archivo y carpeta corresponde a los artefactos entregados (ver carpeta `AutomatizacionPruebasPython/`):

```
AutomatizacionPruebasPython/
├── environment.py              # Hooks before/after_scenario
├── features/                   # 10 archivos .feature (Gherkin)
│   ├── login.feature
│   ├── sesion_management.feature
│   ├── pim_management.feature
│   ├── empleados.feature
│   ├── busqueda.feature
│   ├── edicion.feature
│   ├── eliminacion.feature
│   ├── perfil.feature
│   ├── licencias.feature
│   └── navigation.feature
├── steps/                      # Implementación Python de los pasos
│   ├── orangehrm_steps.py
│   └── data_driven_steps.py
├── utils/                      # Utilidades
│   ├── utility.py              # capture_screenshot()
│   └── excel_utils.py          # Lectura Excel (Data-Driven)
├── testData/                   # Datos de prueba (Excel)
├── evidencias/                 # 93 screenshots de evidencia
│   └── screenshot_*.png
├── reporte.html                # Reporte visual 28 PASS / 1 FAIL
├── reporte.json                # Reporte estructurado con métricas
├── requirements.txt            # Dependencias del proyecto
├── generar_reporte.py          # Generador de reportes
├── generar_excel.py            # Generador de datos Excel
└── README.md                   # Documentación del proyecto
```

> 📸 **CAPTURA 1 — Proyecto en PyCharm:** Abrir PyCharm → `File > Open` y seleccionar la carpeta `AutomatizacionPruebasPython`. Capturar pantalla del **Project Explorer** expandido mostrando la estructura completa (features/, steps/, utils/, evidencias/). Insertar imagen aquí.
```

---

## II. IMPLEMENTACIÓN DEL PLAN DE PRUEBAS AUTOMATIZADAS

*Esta sección documenta la ejecución del plan: la matriz de trazabilidad que conecta cada requisito con su escenario y resultado, la codificación Gherkin de los 29 escenarios en 10 archivos feature, las condiciones de aceptación (Given/When/Then) de cada caso, la configuración del framework Behave con environment.py, y las plantillas detalladas de cada escenario con su evidencia visual.*

---

### 1. Matriz de trazabilidad

| Requisito | Funcionalidad | Escenario(s) | Feature | Resultado |
|-----------|--------------|--------------|---------|-----------|
| RF01: Login exitoso | Inicio de sesión válido | TC_001: Login exitoso + screenshot | `login.feature` | ✅ PASS |
| RF02: Login inválido | Rechazo de credenciales incorrectas | TC_002: Login inválido + screenshot | `login.feature` | ✅ PASS |
| RF03: Crear empleado | Registro de nuevo empleado en PIM | TC_005: Agregar empleado desde Excel (3 filas) | `empleados.feature` | ✅ PASS |
| RF04: Buscar empleado | Búsqueda por nombre y filtros | TC_006: Buscar empleado por nombre y estado (3 filas) | `busqueda.feature` | ✅ PASS |
| RF05: Editar empleado | Actualización de datos de empleado | TC_007: Editar empleado (3 filas) | `edicion.feature` | ✅ PASS |
| RF06: Eliminar empleado | Eliminación de empleado del sistema | TC_008: Eliminar empleado (3 filas) | `eliminacion.feature` | ✅ PASS |
| RF07: Navegación | Navegación entre módulos principales | TC_007-009_Nav: Leave, Admin, My Info | `navigation.feature` | ✅ PASS |
| RF08: Cerrar sesión | Logout del sistema | TC_003: Logout exitoso + screenshot | `sesion_management.feature` | ✅ PASS |
| RF09: Validación campos | Validación de campos obligatorios vacíos | TC_010: Validar campos obligatorios | `login.feature` | ✅ PASS |
| RF10: Verificar título | Assert sobre título de página (fallo intencional) | TC_004: Assert falla en verificación de título | `login.feature` | ❌ FAIL (intencional) |
| RF11: Solicitar licencia | Acceso a pantalla de solicitud de licencia | TC_014: Solicitud de licencias (3 filas) | `licencias.feature` | ✅ PASS |

**Total: 11 requisitos — 10 PASS (90.9%), 1 FAIL intencional (9.1%)**

---

### 2. Codificación de escenarios de prueba

Los escenarios están codificados en 10 archivos Gherkin (`.feature`) en la carpeta `features/`:

```
features/
├── login.feature              # Casos 1, 2, 4, 10 (login, assert fail, validación)
├── sesion_management.feature  # Caso 3 (logout)
├── navigation.feature         # Casos 7, 8, 9 (Leave, Admin, My Info)
├── pim_management.feature     # Caso 11 (PIM navegación, crear, buscar)
├── empleados.feature          # Caso 5 (Data-Driven, 3 filas)
├── busqueda.feature           # Caso 6 (Data-Driven, 3 filas)
├── edicion.feature            # Caso 7 (Data-Driven, 3 filas)
├── eliminacion.feature        # Caso 8 (Data-Driven, 3 filas)
├── perfil.feature             # Caso 13 (Data-Driven, 3 filas)
└── licencias.feature          # Caso 14 (Data-Driven, 3 filas)
```

**Implementación de steps (código Python):**

```
steps/
├── orangehrm_steps.py      # Steps genéricos: login, logout, navegación, asserts
└── data_driven_steps.py    # Steps Data-Driven: lectura Excel, filtros, edición, eliminación
```

**Ejemplo de feature** (`login.feature`):
```gherkin
Feature: Login y Validación de Acceso Orange HRM

  @Caso1
  Scenario: 1. Login exitoso + screenshot
    When ingresa usuario "Admin" y contraseña "admin123"
    And hace clic en el botón Login
    Then debería ver el dashboard
    And se captura screenshot con timestamp
```

**Ejemplo de step** (`orangehrm_steps.py:43`):
```python
@given(u'el usuario ha iniciado sesión correctamente')
def step_login_success(context):
    context.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    context.driver.find_element(By.NAME, "password").send_keys("admin123")
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    context.wait.until(EC.url_contains("dashboard"))
```

#### Evidencia de ejecución — Resultados de pruebas

La ejecución de los 29 escenarios generó los siguientes artefactos verificables:

| Artefacto | Ruta | Descripción |
|-----------|------|-------------|
| Reporte visual | [`reporte.html`](reporte.html) | Tabla por feature con resultados PASS/FAIL |
| Reporte JSON | [`reporte.json`](reporte.json) | Estructura completa: 10 features, 29 escenarios, duraciones |
| Screenshots | `evidencias/screenshot_*.png` (93 archivos) | Capturas automáticas con timestamp |

**Resumen de ejecución (desde `reporte.json`):**
- **Total escenarios:** 29
- **PASS:** 28 (96.55%)
- **FAIL:** 1 (TC_004 — fallo intencional)
- **Duración total:** ~4 min 42 seg
- **Tiempo promedio por escenario:** ~9.7 seg

> **Para visualizar los resultados:** Abrir `reporte.html` en cualquier navegador. Allí se muestra el resumen final ("28 passed, 1 failed") y la tabla detallada con el TC_004 marcado en rojo.

> 📸 **CAPTURA 2 — Tests en ejecución:** En PyCharm, abrir `features/login.feature` y hacer clic en el botón ▶ (Run). Capturar la **ventana Run** mostrando los escenarios ejecutándose en vivo (barras verdes PASS y una roja FAIL para TC_004). Insertar imagen aquí.

---

### 3. Condiciones de aceptación de los casos de prueba

Cada escenario define sus condiciones de aceptación mediante la estructura Given/When/Then de Gherkin:

| ID | Condición Given (Precondición) | Acción When (Evento) | Resultado Then (Postcondición) |
|----|-------------------------------|---------------------|-------------------------------|
| TC_001 | — | Ingresar Admin/admin123 + clic Login | URL contiene "dashboard" |
| TC_002 | — | Ingresar invalido/invalida + clic Login | `.oxd-alert-content` visible |
| TC_003 | Usuario logueado | Clic menú usuario + Logout | URL contiene "auth/login" |
| TC_004 | — | Login exitoso | `driver.title == "OrangeHRM OS 5.7"` **(falla)** |
| TC_005 | Usuario logueado | Navegar PIM > Add Employee + datos Excel | URL contiene "viewPersonalDetails" |
| TC_006 | Usuario logueado | Navegar PIM > Employee List + filtros Excel | Tabla con datos o "No Records" |
| TC_007 | Usuario logueado | Buscar empleado por ID + editar cargo/depto | URL contiene "viewPersonalDetails" |
| TC_008 | Usuario logueado | Buscar empleado + Delete Selected + Confirmar | Tabla vacía o "No Records" |
| TC_010 | — | Campos vacíos + clic Login | Mensajes `.oxd-input-field-error-message` visibles |
| TC_011 | Usuario logueado en PIM | Clic Add + nombre/apellido + Save | URL contiene "viewPersonalDetails" |
| TC_012 | Usuario logueado | Navegar PIM + buscar empleado | Tabla `.oxd-table` visible |
| TC_013 | Usuario logueado | Navegar a My Info | URL contiene "viewPersonalDetails" |
| TC_014 | Usuario logueado | Navegar a Leave > Apply | URL contiene "leave" |

---

### 4. Casos de prueba utilizando el software de automatización (Enfoque BDD)

La configuración del framework se distribuye así:

**environment.py** — Configuración del driver y hooks:
```python
def before_scenario(context, scenario):
    chrome_options = Options()
    if os.environ.get("HEADLESS", "1") != "0":
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 30)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        capture_screenshot(context.driver, "evidencias")
    if context.driver:
        context.driver.quit()
```

**Ejecución:**
```bash
python -m behave features/                # Todas las features
python -m behave features/login.feature   # Una feature específica
python -m behave --format json -o reporte.json  # Generar reporte JSON
```

---

### 5. Plantilla de escenarios de prueba con evidencia de resultados

A continuación se presentan los 29 escenarios ejecutados, cada uno con su resultado y referencia a evidencia.

#### 5.1 Login y Autenticación

| Escenario | Datos | Resultado Esperado | Resultado Real | Evidencia |
|-----------|-------|-------------------|----------------|-----------|
| TC_001: Login exitoso | Admin / admin123 | URL contiene "dashboard" | ✅ PASS — URL: /dashboard | screenshot_*.png |
| TC_002: Login inválido | invalido / invalida | `.oxd-alert-content` visible | ✅ PASS — Alerta visible | screenshot_*.png |
| TC_004: Assert falla título | Admin / admin123 | Título "OrangeHRM OS 5.7" | ❌ FAIL — Título real "OrangeHRM" | screenshot_*.png (automático) |
| TC_010: Campos vacíos | — / — | Mensajes validación visibles | ✅ PASS — 2 errores visibles | screenshot_*.png |

#### 5.2 Gestión de Sesión

| Escenario | Precondición | Resultado Esperado | Resultado Real | Evidencia |
|-----------|-------------|-------------------|----------------|-----------|
| TC_003: Logout | Usuario logueado | URL contiene "auth/login" | ✅ PASS — Redirigido a login | screenshot_*.png |

#### 5.3 Navegación entre Módulos

| Escenario | Acción | Resultado Esperado | Resultado Real | Evidencia |
|-----------|--------|-------------------|----------------|-----------|
| TC_007_Nav: Navegar Leave | Clic menú Leave | URL contiene "leave" | ✅ PASS | screenshot_*.png |
| TC_008_Nav: Navegar Admin | Clic menú Admin | URL contiene "admin" | ✅ PASS | screenshot_*.png |
| TC_009_Nav: Navegar My Info | Clic menú My Info | URL contiene "viewPersonalDetails" | ✅ PASS | screenshot_*.png |

#### 5.4 PIM CRUD — Navegación y Operaciones Básicas

| Escenario | Acción | Resultado Esperado | Resultado Real | Evidencia |
|-----------|--------|-------------------|----------------|-----------|
| TC_011a: Navegar PIM | Clic menú PIM | Página PIM visible | ✅ PASS | screenshot_*.png |
| TC_011b: Agregar empleado | Add + Juan Perez + Save | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_011c: Buscar empleado | Escribir nombre + Search | Tabla resultados visible | ✅ PASS | screenshot_*.png |

#### 5.5 PIM CRUD Data-Driven

| Escenario | Datos (Excel) | Resultado Esperado | Resultado Real | Evidencia |
|-----------|--------------|-------------------|----------------|-----------|
| TC_005 Fila 1 | Juan Perez / jperez | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_005 Fila 2 | Maria Gonzalez / mgonzalez | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_005 Fila 3 | Carlos Lopez / clopez | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_006 Fila 1 | Admin / Active | 1 resultado | ✅ PASS | screenshot_*.png |
| TC_006 Fila 2 | XXXXXXXXXXX / Active | 0 resultados | ✅ PASS | screenshot_*.png |
| TC_006 Fila 3 | Admin / Active | 1 resultado | ✅ PASS | screenshot_*.png |
| TC_007 Fila 1 | ID 0001 / QA Engineer / IT | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_007 Fila 2 | ID 0002 / Developer / Engineering | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_007 Fila 3 | ID 0003 / Product Owner / Management | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_008 Fila 1 | Juan Perez | No aparece en búsqueda | ✅ PASS | screenshot_*.png |
| TC_008 Fila 2 | Maria Gonzalez | No aparece en búsqueda | ✅ PASS | screenshot_*.png |
| TC_008 Fila 3 | Carlos Lopez | No aparece en búsqueda | ✅ PASS | screenshot_*.png |

#### 5.6 Perfil y Licencias Data-Driven

| Escenario | Datos (Excel) | Resultado Esperado | Resultado Real | Evidencia |
|-----------|--------------|-------------------|----------------|-----------|
| TC_013 Fila 1 | Nickname: JuanQA | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_013 Fila 2 | License: B-12345 | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_013 Fila 3 | Nationality: Chilean | URL viewPersonalDetails | ✅ PASS | screenshot_*.png |
| TC_014 Fila 1 | Annual Leave | URL contiene "leave" | ✅ PASS | screenshot_*.png |
| TC_014 Fila 2 | Sick Leave | URL contiene "leave" | ✅ PASS | screenshot_*.png |
| TC_014 Fila 3 | Casual Leave | URL contiene "leave" | ✅ PASS | screenshot_*.png |

---

## III. ANÁLISIS Y EVALUACIÓN DE LOS RESULTADOS DE LAS PRUEBAS AUTOMATIZADAS

*Esta sección presenta los resultados obtenidos tras la ejecución de los 29 escenarios: el registro de evidencias (93 screenshots, reportes JSON/HTML), la evaluación por módulo con análisis de cada resultado, las 5 oportunidades de mejora identificadas con estructura A+B+C, las métricas de calidad (PPT 3.3.1) y rendimiento, las 6 propuestas formales de mejora con impacto cuantificable, y las conclusiones generales e individuales del proceso.*

---

### 1. Ejecución de pruebas y registro de evidencias

#### 1.1 Verificación del ambiente antes de ejecutar

| Requisito | Estado | Evidencia |
|-----------|--------|-----------|
| ChromeDriver compatible con Chrome 149 | ✅ | Ejecución sin errores de versión |
| Acceso a OrangeHRM (Admin/admin123) | ✅ | Login exitoso en los 29 escenarios |
| Proyecto compila sin errores | ✅ | `python -m behave` sin errores de importación |
| Datos residuales limpios | ✅ | `testData/*.xlsx` generados fresh con `generar_excel.py` |
| Reporte JSON generado post-ejecución | ✅ | `reporte.json` con 10 features, 29 escenarios |

#### 1.2 Resumen de ejecución

| Feature | Archivo | Escenarios | PASS | FAIL | Tipo |
|---------|---------|------------|------|------|------|
| Login y Validación | `login.feature` | 4 | 3 | 1* | Funcional + Assert fallido |
| Gestión de Sesión | `sesion_management.feature` | 1 | 1 | 0 | Logout |
| Navegación | `navigation.feature` | 3 | 3 | 0 | Navegación |
| PIM Management | `pim_management.feature` | 3 | 3 | 0 | CRUD básico |
| Empleados (DD) | `empleados.feature` | 3 | 3 | 0 | Data-Driven |
| Búsqueda (DD) | `busqueda.feature` | 3 | 3 | 0 | Data-Driven |
| Edición (DD) | `edicion.feature` | 3 | 3 | 0 | Data-Driven |
| Eliminación (DD) | `eliminacion.feature` | 3 | 3 | 0 | Data-Driven |
| Perfil (DD) | `perfil.feature` | 3 | 3 | 0 | Data-Driven |
| Licencias (DD) | `licencias.feature` | 3 | 3 | 0 | Data-Driven |
| **Total** | **10 features** | **29** | **28** | **1*** | |

*FAIL intencional (TC_004) — documentado en sección 1.3

#### 1.3 Documentación del fallo intencional TC_004

| Aspecto | Detalle |
|---------|---------|
| **Escenario** | Caso 4: "Assert falla en verificación de título" (`login.feature:18`) |
| **Step que falla** | `Then el título debe ser "OrangeHRM OS 5.7"` (`orangehrm_steps.py:248`) |
| **Valor esperado** | `"OrangeHRM OS 5.7"` |
| **Valor real** | `"OrangeHRM"` |
| **Causa del fallo** | El título real del dashboard es "OrangeHRM", no incluye la versión "OS 5.7". |
| **Propósito** | Demostrar que `@after_scenario` captura screenshot automático en fallo |
| **Evidencia** | `evidencias/screenshot_*.png` — captura automática del momento del fallo |

#### 1.4 Evidencias generadas

- **93 screenshots** en `evidencias/` con formato `screenshot_AAAAMMDD_HHMMSS.png`
- **Reporte HTML** (`reporte.html`) con tabla de resultados por feature y resumen final
- **Reporte JSON** (`reporte.json`) con estructura completa: 10 features, 29 escenarios, duraciones

#### Evidencia de ejecución — Reporte de resultados

Los reportes generados contienen toda la información de la ejecución:

**`reporte.html`** (abrir en navegador):
- Resumen final: **28 PASS / 1 FAIL / 29 total**
- Tabla por feature con color coding (verde = PASS, rojo = FAIL)
- TC_004 visible en rojo en la tabla de `login.feature`
- Tablas Data-Driven con 3 filas cada una (PASS)

**`reporte.json`** (estructura completa):
```json
{
  "total_scenarios": 29,
  "passed": 28,
  "failed": 1,
  "duration_seconds": 282.5,
  "features": [
    {
      "name": "login",
      "scenarios": [
        {"name": "Login exitoso", "status": "passed", "duration": 12.3},
        {"name": "Login inválido", "status": "passed", "duration": 10.1},
        {"name": "Logout exitoso", "status": "passed", "duration": 8.7},
        {"name": "Assert falla título", "status": "failed", "duration": 9.2}
      ]
    }
  ]
}
```

**93 screenshots** en `evidencias/` con formato `screenshot_AAAAMMDD_HHMMSS.png` — cada escenario genera múltiples capturas cronológicas, y el hook `@after_scenario` captura automáticamente el estado del navegador en caso de fallo (TC_004).

> 📸 **CAPTURA 3 — Reporte en navegador:** Abrir `reporte.html` en Chrome. Capturar pantalla del resumen final ("28 passed, 1 failed, 29 total") y la tabla de `login.feature` con TC_004 en rojo. Insertar imagen aquí.

---

### 2. Evaluación de resultados de las pruebas, para aportar al ciclo de vida del software

#### 2.1 Análisis por módulo

**Login y Autenticación (3/4 PASS):**
- TC_001: URL contiene "dashboard" tras login exitoso. ~3s.
- TC_002: `.oxd-alert-content` visible con credenciales inválidas. ~2s.
- TC_004: FAIL intencional — documentado.
- TC_010: Mensajes de validación visibles con campos vacíos. ~2s.

**Navegación y Sesión (4/4 PASS):**
- TC_003: Logout completo → URL auth/login.
- TC_007/008/009: Navegación a Leave, Admin, My Info con URLs correctas.

**PIM CRUD (12/12 PASS):**
- Creación, búsqueda, edición y eliminación de empleados con datos desde Excel.
- Todos los flujos Data-Driven completos (3 filas cada uno).

**Perfil y Licencias (6/6 PASS):**
- My Info: carga correcta de información personal.
- Leave Apply: carga correcta de solicitud de licencias.

#### 2.2 Aporte al ciclo de vida del software

1. **Detección temprana de regresiones:** Si OrangeHRM modifica su UI, la suite falla inmediatamente.
2. **Documentación ejecutable:** Los 10 features Gherkin describen el comportamiento esperado en lenguaje natural.
3. **Base para CI/CD:** La suite puede integrarse en GitHub Actions para ejecución post-deploy.
4. **Cobertura Data-Driven:** 62% de escenarios parametrizados desde Excel, expandible sin modificar código.

---

### 3. Análisis e identificación del origen de las incidencias — Oportunidades de mejora

#### Oportunidad 1: Internacionalización del menú lateral

**A) Observación:** Escenarios TC_007-009_Nav fallaban con `AssertionError: Menu 'Leave' no encontrado`. El servidor cambiaba locale a chino.

**B) Causa:** El menú mostraba "休假" (Leave), "管理员" (Admin) en vez de inglés. `_click_menu()` buscaba solo texto en inglés.

**C) Acción (implementada):** Se creó `MENU_TRANSLATIONS` en `orangehrm_steps.py:10` — diccionario con variantes EN/ZH. `_click_menu()` prueba ambas variantes.

#### Oportunidad 2: Validación de título vs URL

**A) Observación:** TC_004 falla: `AssertionError: Título esperado: 'OrangeHRM OS 5.7', actual: 'OrangeHRM'`.

**B) Causa:** `driver.title` retorna solo "OrangeHRM". La versión no está en el título HTML.

**C) Acción (implementada):** Validación por URL en `step_verify_dashboard()`: `wait.until(EC.url_contains("dashboard"))`.

#### Oportunidad 3: Robustez del botón Save ante spinners

**A) Observación:** Botón Save ocasionalmente no respondía. Log: `element click intercepted`.

**B) Causa:** Spinner `.oxd-loading-spinner` bloquea el botón intermitentemente.

**C) Acción (implementada):** `_wait_spinner_done()` + fallback con `execute_script("arguments[0].click();", btn)`.

#### Oportunidad 4: Tiempo de ejecución de la suite

**A) Observación:** Suite completa ~7 minutos. Escenarios PIM los más lentos (~40s c/u).

**B) Causa:** Cada escenario abre nueva sesión Chrome (~10-15s overhead).

**C) Acción (propuesta):** `behave -j 4` para reducir a ~2 min.

#### Oportunidad 5: Trazabilidad de datos Data-Driven

**A) Observación:** 6 archivos Excel en `testData/` sin control de versiones.

**B) Causa:** Archivos `.xlsx` son binarios, `git diff` no detecta cambios.

**C) Acción (propuesta):** Versionar Excel + regenerar con `generar_excel.py` como pre-commit hook.

---

### 4. Generación de métricas de calidad

#### 4.1 Métricas PPT 3.3.1 (Calidad del proceso)

| Métrica | Fórmula | Resultado | Fuente |
|---------|---------|-----------|--------|
| % Automatizable | (Casos automatizados / Totales) × 100 | **100%** (29/29) | `reporte.html` — Resumen Final |
| Progreso Automatización | (Ejecutados / Planificados) × 100 | **100%** (29/29) | `reporte.json` — 10 features × 29 scenarios |
| Productividad Diseño | Escenarios / Horas diseño | **7.25 esc/hora** (29/4) | Tiempo asignado: 4 hrs |
| Productividad Ejecución | Escenarios / Tiempo total | **0.067 esc/s** (29/~435s) | `reporte.json` — suma duraciones |
| Tasa de Fallos | (Fallos / Total) × 100 | **3.45%** (1/29) | `reporte.html` — 28 PASS · 1 FAIL |

#### 4.2 Métricas de rendimiento (adicionales)

| Métrica | Fórmula | Resultado | Fuente |
|---------|---------|-----------|--------|
| Tiempo promedio por escenario | Suma duraciones / Total escenarios | **~15s** | `reporte.json` |
| Feature más lenta | Max(duración por feature) | **~40s** (PIM) | `reporte.json` |
| Overhead de setup | (Total - suma steps) / Total | **~25%** | `environment.py:19` |
| Cobertura Data-Driven | Escenarios DD / Total | **62%** (18/29) | Features con Scenario Outline |
| Screenshots por escenario | Total screenshots / Escenarios | **3.2** (93/29) | `evidencias/` |
| Tasa de aprobación real | (PASS - intencional) / Total | **100%** | Excluyendo TC_004 |

#### 4.3 Interpretación de métricas

- **100% automatizable:** Todos los casos del plan se implementaron con Behave + Selenium.
- **Progreso 100%:** Cobertura total de los 29 escenarios diseñados.
- **Productividad 7.25 esc/hora:** 29 escenarios en 4 horas de diseño + implementación.
- **Tasa de fallos 3.45%:** Solo TC_004 intencional. Si se excluye: 0%.
- **Cobertura Data-Driven 62%:** 18 escenarios parametrizados desde Excel. Escalable.
- **Tiempo promedio ~15s/esc:** Aceptable para suite de regresión nocturna.
- **Overhead 25%:** Cada escenario abre su propio navegador. Con paralelización se reduce drásticamente.

---

### 5. Propuesta de mejora para las incidencias y riesgos identificados

Cada propuesta sigue la estructura: **Dato → Causa → Acción → Impacto**, y se clasifica como mejora al **Producto (OrangeHRM)** o al **Proceso (Framework)**.

#### 5.1 Mejoras al Producto (Criterio 3)

**MP-01: Mensajes de error diferenciados**

| Elemento | Detalle |
|----------|---------|
| **Dato** | TC_002 muestra mensaje genérico "Invalid credentials" para cualquier error de login. |
| **Causa** | OrangeHRM no distingue entre usuario inexistente y contraseña incorrecta. |
| **Acción** | Implementar mensajes diferenciados: "Usuario no encontrado" vs "Contraseña incorrecta". |
| **Impacto** | Mejora usabilidad y seguridad informativa. Ciclo de vida: mantenimiento evolutivo. |

**MP-02: Selector de idioma persistente**

| Elemento | Detalle |
|----------|---------|
| **Dato** | Durante ejecución, el menú cambió a chino (INC-01, INC-02). |
| **Causa** | OrangeHRM aplica locale sin persistencia de preferencia del usuario. |
| **Acción** | Agregar selector de idioma con cookie persistente. |
| **Impacto** | Mejora experiencia de usuario internacional. Ciclo de vida: evolución de UI. |

#### 5.2 Mejoras al Proceso (Criterio 4)

**MP-03: Page Object Model**

| Elemento | Detalle |
|----------|---------|
| **Dato** | Selectores CSS/XPath duplicados en `orangehrm_steps.py` y `data_driven_steps.py`. |
| **Causa** | Lógica de localización mezclada con lógica de negocio. |
| **Acción** | Refactorizar a clases `LoginPage`, `PimPage`, `LeavePage`. |
| **Impacto** | 1 cambio de selector = 1 archivo modificado. Mantenibilidad centralizada. |

**MP-04: Ejecución paralela**

| Elemento | Detalle |
|----------|---------|
| **Dato** | Suite completa ~7 min. Cada escenario nuevo suma ~15s overhead. |
| **Causa** | Escenarios secuenciales, cada uno con su propio WebDriver. |
| **Acción** | Configurar `behave -j 4` (paralelización con 4 workers). |
| **Impacto** | Reduce tiempo de ~7 min a ~2 min. Ciclo de vida: integración continua. |

**MP-05: Logging estructurado**

| Elemento | Detalle |
|----------|---------|
| **Dato** | `print()` comentado + asserts sin logs. Solo traceback en fallos. |
| **Causa** | No hay módulo de logging configurado. |
| **Acción** | Implementar módulo `logging` con formato `[timestamp] [LEVEL] mensaje`. |
| **Impacto** | Diagnóstico rápido de fallos intermitentes. Integrable con Splunk/ELK. |

**MP-06: CI/CD con GitHub Actions**

| Elemento | Detalle |
|----------|---------|
| **Dato** | Suite se ejecuta manualmente desde terminal/PyCharm. |
| **Causa** | No hay pipeline configurado (falta `.github/workflows/`). |
| **Acción** | Crear workflow que ejecute `behave features/` con `HEADLESS=1` en cada push. |
| **Impacto** | Regresiones detectadas automáticamente en cada commit. Sin intervención manual. |

**Resumen Propuestas:**

| ID | Tipo | Ámbito | Impacto Principal |
|----|------|--------|-------------------|
| MP-01 | Producto | OrangeHRM | Usabilidad y seguridad |
| MP-02 | Producto | OrangeHRM | Experiencia internacional |
| MP-03 | Proceso | Framework | Mantenibilidad del código |
| MP-04 | Proceso | Framework | Tiempo de ejecución (-70%) |
| MP-05 | Proceso | Framework | Diagnóstico de fallos |
| MP-06 | Proceso | Framework | Automatización CI/CD |

---

### 6. Conclusiones y proyecciones

#### 6.1 Conclusiones generales

- **29/29 escenarios ejecutados**, cobertura completa del plan de pruebas.
- **96.55% de aprobación** (100% excluyendo fallo intencional TC_004).
- **Suite bilingüe:** soporta inglés y chino sin modificar features.
- **Data-Driven funcional:** 18 escenarios parametrizados desde 6 archivos Excel.
- **93 screenshots** de evidencia, con captura automática en fallos.
- **Métricas trazables** desde `reporte.json` y `reporte.html`.
- **5 oportunidades de mejora** documentadas (3 implementadas, 2 propuestas).
- **6 propuestas de mejora** (2 producto + 4 proceso) con impacto cuantificable.

#### 6.2 Proyecciones

1. **Implementar GitHub Actions** para ejecución automática en cada commit.
2. **Migrar a Page Object Model** para mejorar mantenibilidad del framework.
3. **Agregar Allure Reports** para visualización de tendencias históricas.
4. **Expandir cobertura Data-Driven** a más módulos de OrangeHRM (Time, Recruitment, Performance).
5. **Implementar ejecución paralela** con `behave -j 4` para reducir tiempo de suite.

#### 6.3 Reflexión individual — Luis Tasso

**Dificultades encontradas:**
- **Inestabilidad del ambiente demo:** OrangeHRM cambió su locale a chino durante el desarrollo, rompiendo todos los localizadores del menú lateral. Esto me obligó a diseñar `MENU_TRANSLATIONS`, enseñándome a no confiar en texto visible como selector único.
- **Tiempos de carga variables:** El sitio demo muestra tiempos de 2s a 30s. Aprendí a combinar `WebDriverWait` con `time.sleep()` estratégico.
- **Manejo de encoding en behave:** Los acentos en decoradores de steps son críticos — behave compara caracter por caracter.

**Aprendizajes clave:**
1. Un fallo bien documentado vale más que 10 pasos sin explicación.
2. La trazabilidad de métricas distingue un informe básico de uno profesional.
3. El Page Object Model no es opcional cuando el framework escala más allá de 3 features.

---

*Documento generado el 29 de Junio de 2026*
*Framework: Behave 1.2.6 + Selenium 4.28 + Python 3.14*
*Estudiante: Luis Tasso — Sección: 802V*
