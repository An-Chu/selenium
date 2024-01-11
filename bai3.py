from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://vnexpress.net/')

articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
for item in articles:
    try:
        title = item.find_element(By.TAG_NAME, 'h3').text
        description = item.find_element(By.TAG_NAME, 'p').text
        link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')

        print('Title:', title)
        print('Description:', description)
        print('Link:', link)
        print('----------------------')
    except NoSuchElementException:
        print('Error')

driver.close()