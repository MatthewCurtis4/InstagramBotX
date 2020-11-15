#this is from hackathon
# can use it as a reference and for info and help

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
'''
Setting up Chrome options for use - necessary for chrome to be used in Repl.it
'''
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless') # allows for running in a silent window
'''
Defining Selenium WebDriver with Chrome
'''
# chromedriver_path = *FILE DIRECTORY PATH TO chrome.exe*
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
'''
Input username and password to the page
Find and "click" the login button
'''
#When on the login page webdriver puts curser into the username and password boxes and sends key typing into the boxes
username = webdriver.find_element_by_name('username')
username.send_keys('dumbdumbaccount876') # INSERT USERNAME HERE
password = webdriver.find_element_by_name('password')
password.send_keys('SomePassword1234') # INSERT PASSWORD HERE

LOGIN_BUTTON_XPATH = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button'
button_login = webdriver.find_element_by_xpath(LOGIN_BUTTON_XPATH)
button_login.click()  #after inputting the login data program clicks login
sleep(3) #sleep to buffer the page loading

hashtag_list = ['Adidas']  #list of hashtags to use when searching through insta
new_followed = []  #keeps track of the newly followed accounts
followed = 0  #keeps track of the number of followed
'''
Loop through hashtag list for search material
'''
for tag in hashtag_list:
    print("IN HASHTAG ARRAY")
    webdriver.get(
        'https://www.instagram.com/explore/tags/' + tag +
        '/')  #pulls the URL for the search using one of the hastags
