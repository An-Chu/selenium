from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get('http://www.google.com')

str = input("Input your key: ")
inp = driver.find_element(By.NAME, 'q')
inp.send_keys(str)
inp.submit()
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

for item in results:
    try:

        title = item.find_element(By.TAG_NAME, 'a').text
        link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(title)
        print(link)
        print("---------------------")
    except StaleElementReferenceException:
        print("err")



print(driver.title)



driver.close()