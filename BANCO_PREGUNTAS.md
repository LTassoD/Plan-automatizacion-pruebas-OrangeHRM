# Banco de Preguntas — Defensa Evaluación Final Transversal
**Estudiante:** Luis Tasso | **Sección:** 802V | **Stack:** Behave + Python + Selenium

---

## Preguntas sobre el Stack Tecnológico (reemplaza Maven/Eclipse)

### Q1: ¿Por qué usaste Python con Behave en vez de Java con Cucumber y Maven?
> "Usé Python con Behave porque permite un desarrollo más rápido y el código es más legible para automatización de pruebas. Behave es el equivalente directo de Cucumber para Python: usa el mismo estándar Gherkin. La sintaxis dinámica de Python reduce el boilerplate comparado con Java. Además, herramientas como openpyxl para manejo de Excel tienen una API más simple. El profesor autorizó este stack al inicio del semestre."

### Q2: ¿Cómo gestionas las dependencias del proyecto sin Maven?
> "Uso `requirements.txt` con `pip install -r requirements.txt`. Es el equivalente de Maven para Python. Las dependencias principales son behave 1.2.6, selenium 4.28.0 y openpyxl 3.1. No necesito un archivo POM porque pip maneja la resolución de dependencias de forma más simple."

### Q3: ¿Cómo configuraste Behave? ¿Qué archivos de configuración usas?
> "Behave no requiere un archivo de configuración obligatorio, pero usamos `environment.py` para configurar los hooks. Ahí definimos `before_scenario` que abre el navegador Chrome, configura el timeout, y navega a OrangeHRM. Y `after_scenario` que cierra el navegador y captura screenshot si falló. También uso variables de entorno como `HEADLESS=0` para modo visual."

### Q4: ¿Cómo ejecutas las pruebas? ¿Qué comandos de Behave conoces?
> "Los principales comandos son: `python -m behave` para ejecutar toda la suite; `python -m behave features/login.feature` para una feature específica; `--format json -o reporte.json` para generar reporte; `--tags=Caso1` para filtrar por tag; y propongo `-j 4` para ejecución paralela aunque no lo implementamos aún."

---

## Preguntas sobre el Diseño del Proyecto

### Q5: Explica la estructura general del proyecto Behave.
> "Behave requiere una estructura específica: la carpeta `features/` contiene los archivos `.feature` con escenarios Gherkin. La carpeta `steps/` contiene el código Python que implementa cada paso Given/When/Then. El archivo `environment.py` en la raíz maneja los hooks de ciclo de vida (before/after scenario, before/after feature). Además, tenemos `utils/` para utilidades como lectura de Excel y captura de screenshots, y `testData/` para los archivos Excel con datos de prueba."

### Q6: ¿Cómo funciona la interacción entre los features, los steps y el driver?
> "Behave lee el archivo `.feature` línea por línea. Cada línea Given/When/Then se convierte en un paso que busca un decorador coincidente en los archivos `steps/`. Por ejemplo, el paso `Given el usuario ha iniciado sesión correctamente` se mapea al decorador `@given(u'el usuario ha iniciado sesión correctamente')`. El objeto `context` se pasa entre todos los steps del mismo escenario y transporta el `driver` de Selenium, el `wait` de WebDriverWait, y cualquier dato compartido. El driver se inicializa en `before_scenario` y se destruye en `after_scenario`."

### Q7: ¿Qué ventajas tiene el enfoque BDD frente a pruebas tradicionales?
> "BDD permite que los escenarios sean legibles por stakeholders no técnicos, porque están escritos en lenguaje natural con Given/When/Then. También sirve como documentación viva del sistema: si un escenario falla, sabemos exactamente qué funcionalidad se rompió. Además, los mismos escenarios se usan para pruebas de regresión, de humo y de aceptación."

---

## Preguntas sobre Data-Driven Testing

### Q8: ¿Cómo implementaste Data-Driven Testing?
> "Usamos `Scenario Outline` en Gherkin con `Examples` que referencian números de fila. Luego en el step Python, leemos los datos desde un archivo Excel usando nuestra clase `ExcelUtils`. Por ejemplo, `empleados.feature` tiene 3 filas de Examples. Cada fila ejecuta el mismo escenario pero con datos diferentes: Juan Perez, Maria Gonzalez, Carlos Lopez. Esto nos permite multiplicar la cobertura sin duplicar código."

### Q9: ¿Por qué Excel y no CSV o JSON?
> "Excel permite estructurar los datos en pestañas, lo que facilita organizar diferentes conjuntos de prueba. Además, el profesor puede abrir y modificar los datos sin conocimientos técnicos. Usamos openpyxl que es la biblioteca estándar de Python para Excel. CSV sería más liviano pero menos organizado; JSON sería más técnico."

### Q10: ¿Cómo aseguras que los datos del Excel estén sincronizados con la ejecución?
> "Regeneramos los archivos Excel con `generar_excel.py` antes de cada ejecución. Esto garantiza que los datos sean siempre los mismos. Además, los Excel están versionados en Git, aunque reconocemos que al ser binarios no permiten diff. Por eso propusimos como mejora generar los datos como paso pre-ejecución."

---

## Preguntas sobre el Fallo Intencional TC_004

### Q11: ¿Por qué incluiste un fallo intencional?
> "El curso exige demostrar que el mecanismo de captura de evidencia funciona. El TC_004 espera que el título sea 'OrangeHRM OS 5.7' pero el título real es 'OrangeHRM'. Cuando falla, el hook `after_scenario` en `environment.py` detecta `scenario.status == 'failed'` y ejecuta `capture_screenshot()`, guardando la imagen del momento exacto del fallo en la carpeta `evidencias/`. Esto prueba que el framework registra evidencia incluso en escenarios fallidos."

### Q12: ¿No sería mejor corregir el assert en lugar de dejarlo fallar?
> "Para producción, sí. De hecho, implementamos una solución de validación por URL en `step_verify_dashboard()` que usa `url_contains('dashboard')` en vez de título. Pero para la evaluación, el fallo intencional tiene valor pedagógico: demuestra que el pipeline de captura de evidencia funciona de principio a fin."

---

## Preguntas sobre la Internacionalización (Menú en Chino)

### Q13: ¿Cómo manejaste el cambio de idioma del servidor?
> "Implementamos un diccionario `MENU_TRANSLATIONS` que mapea cada nombre de menú en inglés a sus variantes en chino simplificado. Por ejemplo: 'Leave' → ['Leave', '休假'], 'Admin' → ['Admin', '管理员']. La función `_click_menu()` obtiene todas las etiquetas del menú lateral y compara contra las variantes. Si encuentra coincidencia, hace clic. Esto hace la suite resistente al locale del servidor."

### Q14: ¿Por qué no usaste el atributo `lang` del HTML?
> "El atributo `lang` en OrangeHRM no cambia cuando el servidor cambia el locale. La única diferencia visible está en el texto de los elementos del menú. Por eso tuvimos que usar el texto visible como referencia, pero con el diccionario de traducción como capa de abstracción."

---

## Preguntas sobre Métricas

### Q15: Explica las 5 métricas del PPT 3.3.1 y cómo las calculaste.
> "1) % Automatizable: 29 casos automatizados de 29 totales = 100%, fuente en `reporte.html`. 2) Progreso: 29 ejecutados de 29 planificados = 100%, fuente en `reporte.json`. 3) Productividad de diseño: 29 escenarios en 4 horas de diseño = 7.25 escenarios/hora. 4) Productividad de ejecución: 29 escenarios en ~435 segundos = 0.067 escenarios/s, calculado desde las duraciones en `reporte.json`. 5) Tasa de fallos: 1 fallo de 29 = 3.45%, fuente en `reporte.html`."

### Q16: ¿Qué métricas de rendimiento adicionales presentaste?
> "Tiempo promedio por escenario (~15s), overhead de setup (~25%), cobertura Data-Driven (62%), feature más lenta (PIM ~40s), y screenshots por escenario (~6.1). Estas métricas permiten identificar cuellos de botella y planificar optimizaciones como la ejecución paralela."

---

## Preguntas sobre Propuestas de Mejora

### Q17: ¿Cuál de las 6 propuestas consideras más importante y por qué?
> "Page Object Model (MP-03). Hoy los selectores CSS/XPath están dispersos en 2 archivos de steps. Si OrangeHRM cambia una clase CSS, tenemos que modificar múltiples funciones. Con Page Object, cada página tiene una clase que encapsula sus selectores. Un cambio de selector se hace en un solo lugar. Es la base para que el framework sea mantenible a largo plazo."

### Q18: ¿Cómo implementarías CI/CD con GitHub Actions?
> "Crearía un archivo `.github/workflows/test.yml` que se ejecute en cada push a main. El workflow instalaría Python y las dependencias, configuraría Chrome y ChromeDriver, ejecutaría `python -m behave features/` con `HEADLESS=1`, y publicaría `reporte.html` como artefacto descargable. Así cada commit genera un reporte de regresión automático."

---

## Preguntas sobre el Reporte y Evidencias

### Q19: ¿Cómo generaste el reporte HTML?
> "Behave genera un JSON con `--format json -o reporte.json`. Luego, el script `generar_reporte.py` en Python lee ese JSON, construye una tabla HTML con los resultados por feature y escenario, y escribe `reporte.html`. El HTML incluye estilos CSS, código de colores verde/rojo para PASS/FAIL, y un resumen final con totales."

### Q20: ¿Cuántas evidencias generaste y dónde se almacenan?
> "177 screenshots en la carpeta `evidencias/`. Cada screenshot tiene formato `screenshot_AAAAMMDD_HHMMSS.png` para orden cronológico. Los screenshots se capturan voluntariamente al final de cada escenario con `capture_screenshot()`, y automáticamente cuando un escenario falla gracias al hook `after_scenario`."

---

## Preguntas sobre la Estructura Interna de los Escenarios

### Q21: Explica la estructura de un escenario Gherkin y cómo se relaciona con el código.
> "Un escenario Gherkin tiene tres partes: Given (precondición), When (acción), Then (resultado esperado). Por ejemplo, en login exitoso: Given 'el usuario ha iniciado sesión correctamente' → step que escribe usuario/clave y hace clic. When 'ingresa usuario...' → step opcional. Then 'debería ver el dashboard' → step que valida URL. Cada step es una función Python con un decorador que coincide exactamente con el texto del feature. El objeto `context` conecta todos los steps del mismo escenario y mantiene el driver de Selenium."

### Q22: ¿Qué es el objeto `context` en Behave?
> "El objeto `context` es un contenedor que se pasa automáticamente entre todos los steps de un mismo escenario. En `before_scenario` le asignamos `context.driver` (el navegador) y `context.wait` (WebDriverWait). Luego, cualquier step puede acceder a `context.driver` para interactuar con la página. También podemos guardar datos temporales como `context._busqueda_esperada` para usarlos entre steps."

---

## Preguntas sobre Limitaciones y Trabajo Futuro

### Q23: ¿Qué limitaciones tiene tu suite actual?
> "Tres principales: 1) Ejecución secuencial — la suite tarda ~7 minutos porque cada escenario abre su propio navegador. 2) Sin Page Object Model — los selectores están dispersos, lo que dificulta el mantenimiento. 3) Sin CI/CD — la ejecución es manual. Estas limitaciones están documentadas como propuestas de mejora MP-03, MP-04 y MP-06."

### Q24: Si pudieras empezar de nuevo, ¿qué harías diferente?
> "Implementaría Page Object Model desde el principio, porque refactorizar 2 archivos de steps en clases separadas es más trabajo que hacerlo bien desde el inicio. También usaría logging estructurado en vez de prints. Y planificaría la ejecución paralela desde el Sprint 1."

---

## Preguntas sobre la Estructura del Informe

### Q25: ¿Cómo está estructurado tu informe final?
> "El informe tiene tres secciones principales alineadas con la rúbrica: I) Plan de Pruebas Automatizadas con presentación del caso, cronograma por sprint, casos de prueba formales, técnicas, tipos de pruebas, herramientas y guiones. II) Implementación con matriz de trazabilidad, codificación Gherkin, condiciones de aceptación y plantillas de escenarios con evidencia. III) Análisis de resultados con métricas de calidad y rendimiento, oportunidades de mejora A+B+C, propuestas Dato→Causa→Acción→Impacto, y conclusiones."

---

## Preguntas sobre conceptos generales

### Q26: ¿Qué es un caso de prueba y cómo se diferencia de un escenario?
> "Un caso de prueba es la definición funcional de qué probar: 'Validar que el login con credenciales válidas redirige al dashboard'. Un escenario es la ejecución concreta con datos específicos. Con Data-Driven, un caso de prueba genera múltiples escenarios, uno por cada fila de datos. Por ejemplo, TC_005 (Registro de empleados) es un caso que genera 3 escenarios (Juan, Maria, Carlos)."

### Q27: ¿Qué criterios usaste para priorizar los casos de prueba?
> "Usé dos criterios: impacto en el negocio y frecuencia de uso. Login (TC_001, TC_002) y PIM CRUD (TC_005-008) son alta prioridad porque son las funcionalidades más usadas de OrangeHRM. Navegación y perfil son media prioridad. El fallo intencional TC_004 es prioridad media porque su objetivo es pedagógico, no funcional."

### Q28: ¿Qué tipos de pruebas de automatización cubriste?
> "Cubrimos pruebas funcionales (todos los TC), pruebas de regresión (la suite completa se puede re-ejecutar), pruebas de humo (login + PIM como mínimo), pruebas de internacionalización (navegación con MENU_TRANSLATIONS), pruebas de validación (campos vacíos TC_010), y un fallo intencional (TC_004) que demuestra la captura de evidencia."

### Q29: ¿Cómo manejaste los tiempos de espera en las pruebas?
> "Combiné dos estrategias: `WebDriverWait` con `expected_conditions` para esperas condicionales (ej: esperar a que un elemento sea clickeable o que la URL contenga un texto), y `time.sleep()` para pausas cortas predecibles (ej: 1 segundo después de un clic en menú). El timeout global está configurado en 30 segundos en `environment.py`. Además, `_wait_spinner_done()` espera activamente a que desaparezca el spinner de carga."

### Q30: ¿Cómo documentaste la trazabilidad entre requisitos y resultados?
> "Usé una matriz de trazabilidad en el informe que mapea cada requisito (RF01-RF11) a su funcionalidad, su escenario Gherkin (TC_XXX), el archivo feature, y el resultado (PASS/FAIL). Cada resultado está verificado contra `reporte.json`. El FAIL intencional está documentado con su causa y propósito."

---

## Resumen: Temas que el profesor puede preguntar

| Tema | Probabilidad | Prepárate para... |
|------|-------------|-------------------|
| Stack tecnológico (vs Maven/Eclipse) | 🔴 Muy alta | Explicar Behave, pip, environment.py |
| Data-Driven Testing | 🔴 Muy alta | ExcelUtils, Scenario Outline, Examples |
| Fallo intencional TC_004 | 🟡 Alta | Captura automática, after_scenario |
| Métricas PPT 3.3.1 | 🟡 Alta | Fórmulas, fuentes verificables |
| Propuestas de mejora | 🟡 Alta | Dato→Causa→Acción→Impacto |
| Estructura del proyecto | 🟡 Alta | Features, steps, environment.py |
| Internacionalización | 🟢 Media | MENU_TRANSLATIONS, _click_menu() |
| Page Object Model | 🟢 Media | Por qué no lo implementaste |
| CI/CD | 🟢 Media | Cómo lo harías con GitHub Actions |
| Condiciones de aceptación | 🟢 Media | Given/When/Then como condiciones |
