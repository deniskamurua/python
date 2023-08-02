# for this we will use chrome
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://truthwireless.co.ke/client/login")

username = driver.find_element(By.NAME, "user_name")
username.send_keys("Kiss")
password = driver.find_element(By.NAME, "password")
password.send_keys("4444")
password.send_keys(Keys.ENTER)

driver.quit()