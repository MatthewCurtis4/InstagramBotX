
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
make an .env file that stores your username and password
if you want to call bot without using .env file. Just call bot
 with InstagramBot('your username here', 'your password here')
 instead of InstagramBot(USER, PASSWORD)
'''
USER = os.getenv('username')
PASSWORD = os.environ.get('pw')

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome(executable_path=r'/mnt/c/Users/mcurt/Downloads/chromedriver.exe')
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(3)
        #in general, to find path just look for a unique identify you can use in inspect html
        username_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)      
        click_login = self.driver.find_element_by_xpath('//button[@type="submit"]').click()   
        sleep(5) #got to sleep so we can make sure it has time to work before it closes
        click_login = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)  
'''
self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click
 example of clicking on page 
to find elements on page that you want bot to click, highlight element you want and inspect element the page.
the html will come up with html highlighted of what you had highlighted
use x path to find a string of text and identify object
right click, copy, the click copy full x path
or you can learn queries and can do something like //a[contains(text(), 'Log in')]
'''

    def get_unfollowers(self):
        



Bot = InstagramBot("Testeraccount41014", "Qmwe321")