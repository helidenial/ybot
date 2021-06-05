from time import sleep
from selenium import webdriver
from random import randrange as rand
from selenium.webdriver.chrome.webdriver import WebDriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

def visit(url, loop, duration=10):
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

    try:
        for i in range(loop):
            try:
                driver.get(url)
                print(url, end=" ")
                sleep(rand(duration, duration+10))
                print('########################################')
                print("visited")
            except:
                driver = webdriver.Chrome()
    except:
        pass
    
    finally:
        if isinstance(driver, WebDriver) != True:
            driver.quit()
            