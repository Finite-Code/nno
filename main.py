from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

NANO_ADDRESS = "nano_1xc1soodwjzypreh4jzme4de15p8ooe9fxreg9pgidm33btyzrnck7nxxpa9"

# Try both possible Chromium binary locations
chromium_paths = ["/usr/bin/chromium-browser", "/usr/bin/chromium"]
chromium_binary = None
for path in chromium_paths:
    if os.path.exists(path):
        chromium_binary = path
        break

if not chromium_binary:
    raise FileNotFoundError("Chromium browser not found in expected locations.")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = chromium_binary

# Try both possible chromedriver locations
chromedriver_paths = ["/usr/bin/chromedriver", "/usr/lib/chromium-browser/chromedriver"]
chromedriver_binary = None
for path in chromedriver_paths:
    if os.path.exists(path):
        chromedriver_binary = path
        break

if not chromedriver_binary:
    raise FileNotFoundError("Chromedriver not found in expected locations.")

service = Service(chromedriver_binary)

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
