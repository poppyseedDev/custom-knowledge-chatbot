from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Set up the driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://www.pisrs.si/Pis.web/cm?idStrani=prevodi")

# Wait for the button to be clickable
table_with_links = driver.find_element(By.TAG_NAME, "table")

links = table_with_links.find_elements(By.TAG_NAME, "a")

# Click on each link
for idx, link in enumerate(links[591::2]):
    print("Link number: ", idx)
    print(link.get_attribute("innerHTML"))
    #sleep(0.5)
    link.click()

    tab_with_links = driver.find_element(By.XPATH, "//*[@id='fileBtns']/div[1]")
    links_in_web = tab_with_links.find_elements(By.TAG_NAME, "a")

    for link in links_in_web:
        print(link)
    #    sleep(0.5)
        link.click()

    driver.back()




#button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click me']")))
#//*[@id="fileBtns"]/div[1]/a[2]/img
#//input[@node-type="searchInput"]

# Click the button
#button.click()

# Close the driver
driver.quit()

