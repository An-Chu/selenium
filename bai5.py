from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, csv

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://lms.ou.edu.vn')


driver.find_element(By.CSS_SELECTOR, '.about-content .main-btn').click()
driver.find_element(By.CSS_SELECTOR, 'form button').click()

selectTag = Select(driver.find_element(By.ID, 'form-usertype'))
selectTag.select_by_index(0)

with open('account.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        u = row['user']
        p = row['password']

driver.find_element(By.NAME,'form-username').send_keys(u)
driver.find_element(By.NAME,'form-password').send_keys(p)
driver.find_element(By.CSS_SELECTOR, 'form button').click()
time.sleep(3)

courses = driver.find_elements(By.CSS_SELECTOR, '.card.dashboard-card')
for c in courses:
    print(c.find_element(By.CSS_SELECTOR, 'span.multiline').text)


driver.close()