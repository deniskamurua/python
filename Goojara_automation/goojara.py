from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.goojara.to/")
search = driver.find_element(By.ID, "putin")
search.send_keys("The blacklist")
time.sleep(2)

movies = driver.find_elements(By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[1]")
movies[0].click()
time.sleep(2)
season1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/button[10]")
season1.click()
time.sleep(2)
episodes = driver.find_elements(By.TAG_NAME, "a")
episodes[1].click()

time.sleep(10)

driver.quit()
