
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
        save_info_bypass = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)  
        noti_bypass = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)


    def get_unfollowers(self):
        #click on username to get to our account
        #if screen gets to a certain width this title disapears and function wont work
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username))\
            .click()
        sleep(1)
        #open following list
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self.retreive_name_list();

        #open followers list
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        followers = self.retreive_name_list();
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)     


    def find_tags(self):
        self.driver.find_element_by_xpath("//a[contains(@placeholder,'Search')]")\
            .click()
        following = self.retreive_name_list();    



    def retreive_name_list(self):
       
        #select where suggested for you pops up at bottom of following if you scroll to fast
        suggestions = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        #running java script through selenium. First part is java script, second is the elemnt
        self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
        sleep(1)

        #define what scroll box is. had to use x path, could not find better identifier
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

        # make function so it scrolls until at bottom. Compare if height of box is greater after
        #you try to scroll. If so you are not at max and keep going
        final_ht, height = 0, 1
        while final_ht != height:
            final_ht = height
            sleep(1)
            #scroll to bottom of scroll box and then return its height
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        #each name is a link on the following list so create a python list of all accounts
        links = scroll_box.find_elements_by_tag_name('a')
        #get text out of links
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names
        #self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
        #    .click()
        #followers = self._get_names()
        #not_following_back = [user for user in following if user not in followers]
        #print(not_following_back)





Bot = InstagramBot('testeraccount41014', 'Qmwe321')
#run python3 -i main.py to open interactive controls where selenium web page stays open
# and you can call your methods to test it
#or can just run something like bot get_unfollowers() here


#Bot.get_unfollowers()




'''

NOTES FOR FINDING ELEMENTS ON PAGE


self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click
 example of clicking on page 
to find elements on page that you want bot to click, highlight element you want and inspect element the page.
the html will come up with html highlighted of what you had highlighted
use x path to find a string of text and identify object
right click, copy, the click copy full x path
or you can learn queries and can do something like //a[contains(text(), 'Log in')]
'''