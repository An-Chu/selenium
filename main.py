from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://vnexpress.net/")

print(driver.title)
articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')

for item in articles:
    try:
        title = item.find_element(By.TAG_NAME, 'h3').text
        description = item.find_element(By.TAG_NAME, 'p').text
        link = item.find_element(By.CSS_SELECTOR, 'h3.title-news a').get_attribute('href')
        print(title)
        print(description)
        print(link)
        print("----------")
    except NoSuchElementException:
        print("err")
driver.close()