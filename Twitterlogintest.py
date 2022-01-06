from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import userdetail

class Webdriver:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='d:\\Python Practice tests\\Web Scrapping\\chromedriver.exe')
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(4)

class Login(Webdriver):
        
    def search(self):
        
        '''Search function will search the email box on Twitter login page and insert the email in it and then it will search for phone
        number box and insert phone number and at last it will search for password box and insert passwrod in it and finally it will login
        into Twitter account of whosoever details are mentioned to logged in.
        '''
        try:
            try:
                self.email_box = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
            except Exception as e:
                print(e, "Unable to find the path for email")
            self.email_box.send_keys(userdetail.login_1.get_email())
            time.sleep(2)  
            self.email_box.send_keys(Keys.ENTER)
            time.sleep(2)
            try:
                self.ph_no = self.driver.find_element(By.XPATH, "//input[@name='text']")
            except Exception as e:
                print(e, 'Unable to find path for phone number')
            self.ph_no.send_keys(userdetail.login_1.get_phone())
            self.ph_no.send_keys(Keys.ENTER)
            time.sleep(3)
            try:
                self.password_box = self.driver.find_element(By.XPATH, "//input[@name='password']")  
            except Exception as e:
                print(e, "Unable to find path for password")     
            self.password_box.send_keys(userdetail.login_1.get_pasword())
            self.password_box.send_keys(Keys.ENTER)
            print('Login successfully')
        except Exception as e:
            print(e, 'The error while logging')
            return 
                               
log = Login()
log.search()
print(log.search.__doc__)   


