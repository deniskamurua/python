from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

USERNAME = "deniskamurua@gmail.com"
PASSWORD = "Deni$6597"
SIMILAR_ACCOUNT = "coding_comedy"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    def login(self):
        self.driver.get(" https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email = self.driver.find_element(By.NAME, 'username')
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(10)
        # followers = self.driver.find_element(By.XPATH,
        #                                      '//*[@id="mount_0_0_D5"]/div/div/div[2]/div/div/div/div[1]/div[1]/div['
        #                                      '2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        # followers.click()

        time.sleep(10)
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CLASS_NAME, "_acan")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
