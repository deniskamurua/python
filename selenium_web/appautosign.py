from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("root")
fname.send_keys(Keys.ENTER)
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("joker")
lname.send_keys(Keys.ENTER)
email = driver.find_element(By.NAME, "email")
email.send_keys("root@gmail.com")
email.send_keys(Keys.ENTER)
# button = driver.find_elements(By.CSS_SELECTOR, "form button")
#button.click()
# driver.quit()