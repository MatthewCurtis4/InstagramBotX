
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
user_name = 'Username'
password = 'Password'

os.chmod('/mnt/c/Users/mcurt/Downloads/chromedriver.exe', 755)
driver = webdriver.Chrome(executable_path=r'/mnt/c/Users/mcurt/Downloads/chromedriver.exe')
driver.get("https://www.facebook.com")

element = driver.find_element_by_id("email")
element.send_keys(user_name)

element = driver.find_element_by_id("pass")
element.send_keys(password)

element.send_keys(Keys.RETURN)

driver.close()
'''

'''
Setting up Chrome options for use - necessary for chrome to be used in Repl.it
'''

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')








class InstagramBot:
    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=r'/mnt/c/Users/mcurt/Downloads/chromedriver.exe')
        self.driver.get("https://www.instagram.com")
        sleep(20)


InstagramBot()

