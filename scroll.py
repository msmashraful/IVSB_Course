from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
url = "https://www.daraz.com.bd/products/large-canvas-tote-bag-for-women-stylish-hobo-shoulder-handbag-purse-fsb-19-i524837316-s2530544211.html"
driver.get(url)

driver.maximize_window()
driver.refresh()
#time.sleep(2)  # Wait for the page to load

height = driver.execute_script("return document.body.scrollHeight")

print(f"Initial page height: {height}")

for i in range(0,height+1200,60):
    driver.execute_script(f"window.scrollTo(0, {i})")
    time.sleep(0.5)  # Wait for the scroll to complete
    
comment = driver.find_elements(By.CLASS_NAME, 'content')   
   
comment_list = []
for i in comment:
    comment_list.append(i.text)

print(comment_list)
driver.quit()   
time.sleep(20)  # Let the user actually see something! 
   