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
chrome_options.binary_location = "/usr/bin/chromium-browser"  # Or "/usr/bin/chromium" if needed

service = Service("/usr/bin/chromedriver")  # Explicitly set chromedriver path

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://freenanofaucet.com/")
    time.sleep(2)
    input_box = driver.find_element(By.ID, "nanoAddr")
    input_box.clear()
    input_box.send_keys(NANO_ADDRESS)
    button = driver.find_element(By.ID, "getNano")
    button.click()
    time.sleep(5)
finally:
    driver.quit()
