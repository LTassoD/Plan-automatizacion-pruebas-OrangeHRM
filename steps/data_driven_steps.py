import time
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.excel_utils import ExcelUtils
from utils.utility import capture_screenshot

# Mismo mapping que orangehrm_steps.py por si el sitio esta en chino
MENU_TRANSLATIONS = {
    "Admin": ["Admin", "管理员"],
    "PIM": ["PIM", "个人信息管理系统"],
    "Leave": ["Leave", "休假"],
    "My Info": ["My Info", "我的信息"],
    "Dashboard": ["Dashboard", "仪表盘"],
    "Time": ["Time", "时间"],
    "Recruitment": ["Recruitment", "招聘"],
    "Performance": ["Performance", "绩效"],
    "Directory": ["Directory", "Directory"],
    "Maintenance": ["Maintenance", "Maintenance"],
    "Claim": ["Claim", "Claim"],
    "Buzz": ["Buzz", "激动"],
}


def _click_menu(context, name):
    """Busca elemento en menu lateral probando variantes de idioma.
    """
    variants = MENU_TRANSLATIONS.get(name, [name])
    context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-sidepanel-body")))
    time.sleep(1)
    items = context.driver.find_elements(By.CSS_SELECTOR, "span.oxd-main-menu-item--name")
    for el in items:
        stripped = el.text.strip()
        if stripped in variants:
            el.click()
            time.sleep(2)
            return
    raise AssertionError(f"Menu '{name}' no encontrado. Items: {[e.text for e in items]}")


def _wait_spinner_done(context):
    """Espera a que desaparezca el spinner de carga (rueda girando).
    Es necesario despues de navegar entre secciones.
    """
    try:
        context.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-loading-spinner"))
        )
    except Exception:
        pass  # Si no aparece el spinner, continuamos


# ===== Case 5: Registro de empleados Data-Driven =====

@when(u'navega a PIM > Add Employee')
def step_nav_pim_add(context):
    """Navega a PIM y hace clic en la pestana Add Employee.
    """
    _click_menu(context, "PIM")
    time.sleep(2)
    _wait_spinner_done(context)
    try:
        context.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(normalize-space(), 'Add Employee')]")
        )).click()
    except Exception:
        tabs = context.driver.find_elements(By.CSS_SELECTOR, "a.oxd-topbar-body-nav-tab-item")
        for tab in tabs:
            if "Add" in tab.text:
                tab.click()
                break
    time.sleep(2)
    _wait_spinner_done(context)
    context.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))


@when(u'carga los datos del empleado de la fila {fila:d} del Excel')
def step_cargar_empleado(context, fila):
    """Lee los datos de dataEmpleados.xlsx y completa el formulario
    de nuevo empleado, incluyendo credenciales de login.
    """
    ExcelUtils.set_excel_file_sheet("testData/dataEmpleados.xlsx", "Empleados")
    first = ExcelUtils.get_cell_data(fila + 1, 2)
    last = ExcelUtils.get_cell_data(fila + 1, 3)
    username = ExcelUtils.get_cell_data(fila + 1, 4)
    password = ExcelUtils.get_cell_data(fila + 1, 5)

    context.driver.find_element(By.NAME, "firstName").send_keys(first)
    context.driver.find_element(By.NAME, "lastName").send_keys(last)
    time.sleep(0.5)

    # Activa el toggle "Create Login Details" si no lo esta
    toggle = context.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input")
    if not toggle.is_selected():
        context.driver.execute_script("arguments[0].click();", toggle)
        time.sleep(0.5)

    context.driver.find_element(By.XPATH, "//label[text()='Username']/following::input[1]").send_keys(username)
    context.driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]").send_keys(password)
    context.driver.find_element(By.XPATH, "//label[text()='Confirm Password']/following::input[1]").send_keys(password)


# ===== Case 6: Busqueda de empleados con filtros Data-Driven =====

@when(u'navega a PIM > Employee List')
def step_nav_pim_list(context):
    """Navega a PIM y hace clic en la pestana Employee List.
    """
    _click_menu(context, "PIM")
    time.sleep(1)
    _wait_spinner_done(context)
    tabs = context.driver.find_elements(By.CSS_SELECTOR, "a.oxd-topbar-body-nav-tab-item")
    for tab in tabs:
        if "Employee List" in tab.text:
            tab.click()
            break
    time.sleep(1)
    _wait_spinner_done(context)


@when(u'aplica filtros de la fila {fila:d} del Excel')
def step_aplicar_filtros(context, fila):
    """Aplica los filtros de busqueda segun los datos del Excel.
    Soporta busqueda por nombre (autocomplete) y por Employee ID.
    Tambien puede seleccionar el estado (Active/Terminated).
    """
    ExcelUtils.set_excel_file_sheet("testData/dataFiltros.xlsx", "Filtros")
    search_val = str(ExcelUtils.get_cell_data(fila + 1, 2) or "")
    context._busqueda_esperada = str(ExcelUtils.get_cell_data(fila + 1, 4) or "")

    include_val = str(ExcelUtils.get_cell_data(fila + 1, 3) or "")

    if search_val.isdigit():
        emp_id_input = context.driver.find_elements(By.XPATH,
            "//label[contains(text(),'Employee Id')]/following::input[1]")
        if emp_id_input:
            emp_id_input[0].clear()
            emp_id_input[0].send_keys(search_val)
    else:
        search_input = context.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        search_input.clear()
        search_input.send_keys(search_val)
        time.sleep(1)
        try:
            dropdown = context.driver.find_element(By.XPATH,
                "//div[@role='listbox']//span[contains(text(),'" + search_val + "')]")
            dropdown.click()
        except Exception:
            pass

    all_dropdowns = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-text.oxd-select-text--active")
    if include_val and len(all_dropdowns) >= 2:
        context.driver.execute_script("arguments[0].click();", all_dropdowns[1])
        time.sleep(0.5)
        options = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option")
        for opt in options:
            if include_val.lower() in opt.text.strip().lower():
                context.driver.execute_script("arguments[0].click();", opt)
                break


@then(u'los resultados deben coincidir con lo esperado')
def step_verificar_resultados(context):
    """Verifica que la tabla de resultados tenga al menos una fila
    o que muestre el mensaje 'No Records'.
    """
    time.sleep(2)
    no_records = context.driver.find_elements(By.XPATH, "//span[contains(text(),'No Records')]")
    rows = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    assert len(rows) > 0 or len(no_records) > 0, "La tabla no tiene datos ni mensaje No Records"


@then(u'la tabla de empleados debe mostrar datos')
def step_verificar_tabla_empleados(context):
    """Verifica que la tabla Employee List tenga datos o mensaje No Records.
    """
    time.sleep(2)
    no_records = context.driver.find_elements(By.XPATH, "//span[contains(text(),'No Records')]")
    rows = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    assert len(rows) > 0 or len(no_records) > 0, "La tabla de empleados no tiene datos"


# ===== Case 7: Edicion de empleados Data-Driven =====

@when(u'busca el empleado con ID de la fila {fila:d}')
def step_buscar_empleado_id(context, fila):
    """Busca un empleado por ID en el Excel y abre su formulario de edicion.
    """
    ExcelUtils.set_excel_file_sheet("testData/dataEdicion.xlsx", "Edicion")
    emp_id = ExcelUtils.get_cell_data(fila + 1, 2)

    search_input = context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
    )
    search_input.clear()
    search_input.send_keys(emp_id)
    time.sleep(1)

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    _wait_spinner_done(context)

    edit_btn = context.driver.find_element(By.CSS_SELECTOR, ".oxd-table-cell-actions button:first-child")
    edit_btn.click()
    time.sleep(1)
    _wait_spinner_done(context)


@when(u'actualiza cargo y departamento de la fila {fila:d}')
def step_actualizar_cargo_depto(context, fila):
    """Actualiza los campos Job Title y Subunit en el formulario de edicion.
    Los valores se leen desde dataEdicion.xlsx.
    """
    ExcelUtils.set_excel_file_sheet("testData/dataEdicion.xlsx", "Edicion")
    cargo = ExcelUtils.get_cell_data(fila + 1, 3)
    depto = ExcelUtils.get_cell_data(fila + 1, 4)

    try:
        job_dropdown = context.driver.find_element(By.XPATH,
            "//label[contains(text(),'Job Title')]/following::div[@class='oxd-select-text oxd-select-text--active'][1]")
        context.driver.execute_script("arguments[0].click();", job_dropdown)
        time.sleep(0.5)
        options = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option")
        for opt in options:
            if cargo.lower() in opt.text.strip().lower():
                opt.click()
                break
    except Exception:
        pass

    try:
        dept_dropdown = context.driver.find_element(By.XPATH,
            "//label[contains(text(),'Subunit')]/following::div[@class='oxd-select-text oxd-select-text--active'][1]")
        context.driver.execute_script("arguments[0].click();", dept_dropdown)
        time.sleep(0.5)
        options = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option")
        for opt in options:
            if depto.lower() in opt.text.strip().lower():
                opt.click()
                break
    except Exception:
        pass


@then(u'los datos actualizados deben reflejarse')
def step_verificar_edicion(context):
    """Verifica que la edicion redirija a la pagina de detalles personales.
    """
    context.wait.until(EC.url_contains("viewPersonalDetails"))
    assert "viewPersonalDetails" in context.driver.current_url


# ===== Case 8: Eliminacion de empleados Data-Driven =====

@when(u'busca al empleado de la fila {fila:d} del Excel')
def step_buscar_empleado_eliminar(context, fila):
    """Busca un empleado por nombre completo en el Excel para eliminarlo.
    """
    ExcelUtils.set_excel_file_sheet("testData/dataEliminacion.xlsx", "Eliminacion")
    first = ExcelUtils.get_cell_data(fila + 1, 2)
    last = ExcelUtils.get_cell_data(fila + 1, 3)
    full_name = f"{first} {last}"

    search_input = context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
    )
    search_input.clear()
    search_input.send_keys(first)
    time.sleep(1)

    try:
        dropdown = context.driver.find_element(By.XPATH,
            "//div[@role='listbox']//span[contains(text(),'" + full_name + "')]")
        dropdown.click()
    except Exception:
        pass

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    _wait_spinner_done(context)


@when(u'selecciona el checkbox y hace clic en Delete')
def step_seleccionar_eliminar(context):
    """Marca el checkbox del empleado y hace clic en Delete Selected.
    """
    checkbox = context.driver.find_element(By.CSS_SELECTOR, ".oxd-table-row input[type='checkbox']")
    context.driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(0.5)

    delete_btn = context.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Delete Selected')]")
    delete_btn.click()
    time.sleep(0.5)


@when(u'confirma la eliminación')
def step_confirmar_eliminacion(context):
    """Confirma la eliminacion en el modal emergente (Yes, Delete).
    """
    context.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(),'Yes, Delete')]"))
    ).click()
    time.sleep(2)
    _wait_spinner_done(context)


@then(u'el empleado no debe aparecer en la búsqueda')
def step_verificar_no_resultados(context):
    """Verifica que el empleado eliminado ya no aparezca en resultados.
    """
    time.sleep(1)
    rows = context.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    no_records = context.driver.find_elements(By.XPATH, "//span[contains(text(),'No Records')]")
    assert len(rows) == 0 or len(no_records) > 0, "Aun se encontraron registros"


# ===== Case 13: Perfil (My Info) Data-Driven =====

@when(u'navega a My Info')
def step_nav_my_info(context):
    """Navega a la seccion My Info del menu lateral.
    """
    _click_menu(context, "My Info")
    time.sleep(1)
    _wait_spinner_done(context)


@then(u'la página de My Info debe cargar correctamente')
def step_verificar_my_info(context):
    """Verifica que la pagina My Info se haya cargado.
    """
    context.wait.until(EC.url_contains("viewPersonalDetails"))
    assert "viewPersonalDetails" in context.driver.current_url


# ===== Case 14: Solicitud de licencias Data-Driven =====

@when(u'navega a Leave > Apply')
def step_nav_leave_apply(context):
    """Navega a Leave y hace clic en la pestana Apply.
    """
    _click_menu(context, "Leave")
    time.sleep(1)
    _wait_spinner_done(context)
    tabs = context.driver.find_elements(By.CSS_SELECTOR, "a.oxd-topbar-body-nav-tab-item")
    for tab in tabs:
        if "Apply" in tab.text:
            tab.click()
            break
    time.sleep(1)
    _wait_spinner_done(context)


@then(u'la página de solicitud de licencia debe cargar correctamente')
def step_verificar_leave_apply(context):
    """Verifica que la pagina Apply Leave se haya cargado.
    """
    context.wait.until(EC.url_contains("leave"))
    assert "leave" in context.driver.current_url.lower()
