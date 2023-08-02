from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

FB_EMAIL = "0791617112"
FB_PASS = "123456789987654321"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://tinder.com/")
time.sleep(15)

login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div['
                                      '2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(10)

fb_login = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div['
                                         '2]/button/div[2]/div[2]/div/div')
fb_login.click()

# navigate to the fb pop up window
time.sleep(10)

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
fb_user = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_user.send_keys(FB_EMAIL)
passwd = driver.find_element(By.XPATH, '//*[@id="pass"]')
passwd.send_keys(FB_PASS)
passwd.send_keys(Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
time.sleep(5)
allow_location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()
time.sleep(5)
cookies = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
time.sleep(5)
notifications = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications.click()
try:
    like = driver.find_element(By.XPATH,
                               '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                               '3]/div/div[4]/button/span/span/svg/path')
    like.click()
except NoSuchElementException:
    time.sleep(2)

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div['
                                          '2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        # FOUND A MATCH CLICK BACK TP TINDER BUTTON
        try:
            match_popup = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div['
                                                        '2]/main/div/div[1]/div/div[3]/button')
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
