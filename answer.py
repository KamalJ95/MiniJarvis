import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome('/Users/kamalj/Downloads/chromedriver')
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Unfortunately this didn't work.")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="Z0LcW")

        if not answer:
            answer = soup.find_all(class_="wUrVib")

        if not answer:
            answer = "I don't know."

        self.driver.quit()
        return answer[0].get_text()




