# auto_script.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

NANO_ADDRESS = "nano_1nxm581mokwpco6egnqgenc3qszae68be3956kcctszkeg3iomy1c45xgj9n"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://freenanofaucet.com/")
    time.sleep(2)  # Wait for page to load

    # Enter Nano address
    input_box = driver.find_element(By.ID, "nanoAddr")
    input_box.clear()
    input_box.send_keys(NANO_ADDRESS)

    # Click the button
    button = driver.find_element(By.ID, "getNano")
    button.click()

    time.sleep(5)  # Wait for any actions to complete
finally:
    driver.quit()
