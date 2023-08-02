from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#count.click()

link = driver.find_element(By.LINK_TEXT, "Create account")
# link.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("root")
search.send_keys(Keys.ENTER)

#driver.close()
