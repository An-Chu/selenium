from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789')
driver.find_element(By.CSS_SELECTOR, '.sort-list a:nth-child(2)').click()
time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, "div[data-view-id='product_list_container'] > :not(.tiki-square-ad)")
for i, p in enumerate(products[:10]):
    print("Product #:", i + 1)
    print(p.find_element(By.CSS_SELECTOR, '.info .name h3').get_attribute("innerText"))
    print(p.find_element(By.CSS_SELECTOR, 'picture img').get_attribute('srcset'))
    print('----------------------')
driver.close()