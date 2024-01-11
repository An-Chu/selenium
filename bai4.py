import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://www.facebook.com/')

time.sleep(1)
driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
time.sleep(1)
driver.find_element(By.NAME, 'firstname').send_keys('Chu')
driver.find_element(By.NAME, 'lastname').send_keys('An')
driver.find_element(By.NAME, 'reg_email__').send_keys('nguyenchuphuocan123@gmail.com')
driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys('nguyenchuphuocan123@gmail.com')
driver.find_element(By.NAME, 'reg_passwd__').send_keys('PhuocAn123!')
dateSelect = Select(driver.find_element(By.NAME, 'birthday_day'))
dateSelect.select_by_visible_text('14')
monthSelect = Select(driver.find_element(By.NAME, 'birthday_month'))
monthSelect.select_by_visible_text('Apr')
yearSelect = Select(driver.find_element(By.NAME, 'birthday_year'))
yearSelect.select_by_visible_text('2002')
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.NAME, 'websubmit').click()

time.sleep(4)


driver.close()