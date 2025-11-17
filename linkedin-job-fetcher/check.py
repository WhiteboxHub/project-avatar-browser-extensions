from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://insightglobal.com/jobs/")
driver.maximize_window()

# Wait for React to mount
time.sleep(5)

# Use XPATH for the input box
xpath_input = "//input[@placeholder='Title or keyword']"

# Wait for input presence
search_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, xpath_input))
)

# Scroll input into view (IMPORTANT)
driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
time.sleep(1)

# Click using JavaScript to avoid intercept error
driver.execute_script("arguments[0].click();", search_box)

# Now type text
search_box.send_keys("QA Engineer")

time.sleep(5)
driver.quit()
