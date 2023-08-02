# using fire_fox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://truthwireless.co.ke/client/login")

username = driver.find_element(By.NAME, "user_name")
username.send_keys("Kiss")
password = driver.find_element(By.NAME, "password")
password.send_keys("4444")
password.send_keys(Keys.ENTER)


