from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.daraz.com.bd/#?")
driver.maximize_window()
tittle = driver.find_element(By.XPATH, '//*[@id="529899010"]/div[2]').text
link = driver.find_element(By.XPATH, '//*[@id="529899010"]').get_attribute('href')

print(tittle, link)
time.sleep(50)  # Let the user actually see something!