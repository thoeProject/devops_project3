# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

# Start the browser and perform the test
def start ():
    print (timestamp() + 'Access to web browser')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()

    # Login
    login(driver, 'standard_user', 'secret_sauce')

    # Add cart
    add_cart(driver)

    # Remove cart
    remove_cart(driver)

# Login method
def login (driver, user, password):
    print (timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    print (timestamp() + 'Input valid user name which is already existed in system')
    driver.find_element(By.CSS_SELECTOR, "input[id = 'user-name']").send_keys(user)

    print (timestamp() + 'Input valid password which is already existed in system')
    driver.find_element(By.CSS_SELECTOR, "input[id = 'password']").send_keys(password)

    print (timestamp() + 'Click Login button')
    driver.find_element(By.CSS_SELECTOR, "input[id = 'login-button']").click()

    logoElements = driver.find_elements(By.CSS_SELECTOR, ".app_logo")
    assert len(logoElements) > 0, "The element not found. Try another element."

    print (timestamp() + 'Login successfully')

# Add cart
def add_cart(driver):
    print (timestamp() + 'Add six products')
    productElements = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    for product in productElements:
        productButton = product.find_element(By.CSS_SELECTOR, ".btn_inventory")
        productName = product.find_element(By.CSS_SELECTOR, ".inventory_item_name")

        print(timestamp() + f"Product {productName.text} is added to cart")
        productButton.click()

    cartCount = int(driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text)
    assert cartCount == len(productElements), 'The quantity in cart does not correct'

    print(timestamp() + 'The quantity in cart is ' + str(cartCount))

# Remove all product
def remove_cart(driver):
    print (timestamp() + 'Access to Cart page')
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    print (timestamp() + 'Remove all products')
    removeButtons = driver.find_elements(By.CSS_SELECTOR, ".cart_button")
    for remove in removeButtons:
        remove.click()

    cartCountElement = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(cartCountElement) == 0, "Item cannot be removed"

    print(timestamp() + 'Item has been removed successfully')

def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    return (ts + ' ')

start()