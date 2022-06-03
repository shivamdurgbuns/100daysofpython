from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

#Uncomment below lines if you want to downlaod and install driver.
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver = webdriver.Firefox(service=Service('/home/sdurgbun/.wdm/drivers/geckodriver/linux64/v0.31.0/geckodriver'))

driver.get("https://www.selenium.dev")

f_element_by_id = driver.find_element(By.ID, "main_navbar")
f_element_by_name = driver.find_element(By.NAME, "submit")
f_element_by_xpath = driver.find_element(By.XPATH, "/html/head/meta[5]")
f_element_by_class = driver.find_element(By.CLASS_NAME,"selenium-button-container")

driver.quit()

print(f"Element with ID gsc-iw-id1 is {f_element_by_id}")
print(f"Element by NAME submit is {f_element_by_name}")
print(f"Location of heading 'Selenium automates browsers. That's it!' is at {f_element_by_xpath}")
print(f"Element by CLASS NAME selenium-button-container is at {f_element_by_class}")