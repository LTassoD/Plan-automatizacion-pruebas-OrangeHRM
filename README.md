# Automatización de Pruebas - OrangeHRM

Proyecto de automatización de pruebas para el sitio **OrangeHRM** ([opensource-demo.orangehrmlive.com](https://opensource-demo.orangehrmlive.com/)) usando **Behave** + **Selenium WebDriver** + **Data-Driven Testing con Excel**.

## Requisitos

- Python 3.14+ (recomendado)
- Google Chrome
- Dependencias (instalar con pip):

```bash
pip install behave selenium openpyxl
```

## Estructura del Proyecto

```
AutomatizacionPruebasPython/
├── features/                    # Archivos .feature (Gherkin - 10 archivos, 29 escenarios)
│   ├── login.feature            # Casos 1, 2, 4, 10
│   ├── sesion_management.feature # Caso 3
│   ├── navigation.feature       # Casos 7, 8, 9
│   ├── pim_management.feature   # Caso 11 (PIM)
│   ├── empleados.feature        # Caso 5 (Data-Driven, 3 filas)
│   ├── busqueda.feature         # Caso 6 (Data-Driven, 3 filas)
│   ├── edicion.feature          # Caso 7 (Data-Driven, 3 filas)
│   ├── eliminacion.feature      # Caso 8 (Data-Driven, 3 filas)
│   ├── perfil.feature           # Caso 13 (Data-Driven, 3 filas)
│   └── licencias.feature        # Caso 14 (Data-Driven, 3 filas)
├── steps/
│   ├── orangehrm_steps.py       # Steps genéricos (login, logout, navegacion, screenshots)
│   └── data_driven_steps.py     # Steps Data-Driven con lectura de Excel
├── utils/
│   ├── utility.py               # Funcion capture_screenshot()
│   └── excel_utils.py           # Clase ExcelUtils para leer archivos .xlsx
├── testData/                    # Archivos Excel con datos de prueba
│   ├── dataEmpleados.xlsx       # Case 5
│   ├── dataFiltros.xlsx         # Case 6
│   ├── dataEdicion.xlsx         # Case 7
│   ├── dataEliminacion.xlsx     # Case 8
│   ├── dataPerfil.xlsx          # Case 13
│   └── dataLicencias.xlsx       # Case 14
├── evidencias/                  # Screenshots generados durante la ejecucion
├── environment.py               # Configuracion del driver (before/after scenario)
├── generar_excel.py             # Genera los archivos Excel de datos de prueba
├── generar_reporte.py           # Convierte reporte.json a reporte.html
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

## Instrucciones de Ejecucion

### 1. Generar datos de prueba (solo la primera vez)

```bash
python generar_excel.py
```

### 2. Ejecutar todas las pruebas (modo headless)

```bash
set HEADLESS=1
python -m behave
```

### 3. Ejecutar una feature especifica

```bash
python -m behave features\login.feature
```

### 4. Ejecutar en modo visual (ver el navegador)

```bash
set HEADLESS=0
python -m behave features\login.feature
```

### 5. Ejecutar desde PyCharm

1. Abrir el proyecto en PyCharm.
2. Configurar el interprete Python: `C:\Users\User\AppData\Local\Python\bin\python.exe`.
3. Crear un Run Configuration:
   - **Module name**: `behave`
   - **Parameters**: `features\login.feature` (o la feature deseada)
   - **Working directory**: ruta del proyecto
   - **Environment variables**: `HEADLESS=0` (para modo visual)
4. Ejecutar.

### 6. Generar reporte HTML

```bash
python -m behave --format json -o reporte.json
python generar_reporte.py
```

Luego abrir `reporte.html` en el navegador.

## Resultados Esperados

| Indicador | Valor |
|-----------|-------|
| Total escenarios | 29 |
| Casos que pasan | 28 |
| Caso que falla (intencional) | 1 (Caso 4: assert de titulo) |
| Features | 10 |
| Screenshots | ~1 por escenario en evidencias/ |

## Solucion de Problemas

- **"No module named behave"**: Verificar que se usa el Python correcto (`C:\Users\User\AppData\Local\Python\bin\python.exe`).
- **Error de timeout**: El sitio OrangeHRM demo puede ser lento. Aumentar el timeout en `environment.py`.
- **Menu no encontrado**: El sitio podria estar en chino. El codigo ya maneja traduccion ingles/chino.
- **"HEADLESS no se reconoce"**: En Windows CMD usar `set HEADLESS=0`, no `HEADLESS=0` sola.

## Notas

- El Caso 4 falla **intencionalmente** para demostrar la captura de screenshots en escenarios fallidos.
- Los datos de prueba estan en archivos Excel dentro de `testData/`.
- Los screenshots se almacenan en `evidencias/` con timestamp.
- El sitio demo se resetea cada 30 minutos, los datos creados pueden perderse.
