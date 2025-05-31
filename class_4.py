from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://www.daraz.pk/invisible-unisex-fashion-3/"

driver.get(url)
driver.maximize_window()
tittle_list = []
for page in range(1, 88):
    driver.get(f"{url}?page={page}")
    for i in range(1, 41):
        j = str(i)
        title = driver.find_element(By.XPATH, 
        f'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j
        +']/div/div/div[2]/div[2]/a').text
        tittle_list.append(title)
    
print(tittle_list)
print(len(tittle_list))   
time.sleep(20)  # Wait for the page to load