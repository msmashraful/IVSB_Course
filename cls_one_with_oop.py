from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class DarazScraper:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def scrape(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)  # Wait for the page to load

        title = self.driver.find_element(By.XPATH, '//*[@id="171444191"]/div[2]/p').text
        link = self.driver.find_element(By.XPATH, '//*[@id="171444191"]').get_attribute('href')

        print(title, link)

    def close(self):
        self.driver.quit()
    
if __name__ == "__main__":
    url = "https://www.daraz.com.bd/#?"
    scraper = DarazScraper(url)
    try:
        scraper.scrape()
    finally:
        time.sleep(50)  # Let the user actually see something!
        scraper.close()
