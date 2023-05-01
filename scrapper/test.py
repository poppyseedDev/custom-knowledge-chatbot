from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Set up the driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://www.pisrs.si/Pis.web/pregledPredpisa?id=ZAKO541")

# Wait for the button to be clickable
tab_with_links = driver.find_element(By.XPATH, "//*[@id='fileBtns']/div[1]")
links = tab_with_links.find_elements(By.TAG_NAME, "a")

for link in links:
    print(link)
    sleep(1)
    link.click()

# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fileBtns']/div[1]")))

#//*[@id="fileBtns"]/div[1]/a[2]/img
