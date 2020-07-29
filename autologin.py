from selenium import webdriver
from confidential import *

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/Vishal/PycharmProjects/automation/chromedriver.exe')

    def edureka(self):
        self.driver.get('https://www.facebook.com/')

        user = self.driver.find_element_by_xpath('//*[@id="email"]')
        user.click()
        user.send_keys(username)

        pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd.click()
        pwd.send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()


bot = Bot()
bot.edureka()
