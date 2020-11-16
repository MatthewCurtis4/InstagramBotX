

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
'''
Setting up Chrome options for use - necessary for chrome to be used in Repl.it
'''
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')



class InstagramBot:
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')

InstagramBot()
