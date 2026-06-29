from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
print("=== LOGIN OK ===")

# Click PIM
driver.find_element(By.PARTIAL_LINK_TEXT, "PIM").click()
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='PIM']")))
print("=== PIM PAGE ===")

# Click Add
try:
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(), 'Add')]")))
    add_btn.click()
    print("=== CLICKED ADD ===")
except Exception as e:
    print(f"Add button error: {e}")
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    for b in all_buttons:
        print(f"  Button text: '{b.text}' class: {b.get_attribute('class')}")

WebDriverWait(driver, 10).until(EC.url_contains("addEmployee"))
print(f"URL after Add: {driver.current_url}")

# Get all inputs
inputs = driver.find_elements(By.CSS_SELECTOR, "input.oxd-input--active")
print(f"\n=== INPUTS FOUND: {len(inputs)} ===")
for i, inp in enumerate(inputs):
    print(f"  Input[{i}]: name='{inp.get_attribute('name')}' placeholder='{inp.get_attribute('placeholder')}' class='{inp.get_attribute('class')}'")

# Get all form elements
print("\n=== FORM HTML ===")
form = driver.find_element(By.TAG_NAME, "form")
print(form.get_attribute("outerHTML")[:3000])

# Check sidebar menu for Leave
print("\n=== SIDEBAR MENU ITEMS ===")
menu_items = driver.find_elements(By.CSS_SELECTOR, "a.oxd-main-menu-item")
for item in menu_items:
    print(f"  href={item.get_attribute('href')} text='{item.text}'")

driver.quit()
