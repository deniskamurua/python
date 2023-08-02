from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://truthwireless.co.ke/client/login")

username = driver.find_element(By.NAME, "user_name")
username.send_keys("Denno_kingpin")
password = driver.find_element(By.NAME, "password")
password.send_keys("1111")
password.send_keys(Keys.ENTER)

time.sleep(5)
packages = driver.find_elements(By.CSS_SELECTOR, ".col-xs-12 a")
packages[1].click()

time.sleep(3)
package = driver.find_elements(By.CSS_SELECTOR, ".panel-heading b")
package[2].click()

time.sleep(30)

account = driver.find_element(By.LINK_TEXT, "My Account")
account.click()

time.sleep(30)
driver.quit()
