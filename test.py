from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import unittest
from time import sleep
import os

class GmailTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['avd'] = "Nexus"
        desired_caps['appPackage'] = 'com.google.android.gm'
        desired_caps['appActivity'] = 'com.google.android.gm.ui.MailActivityGmail'
        
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def testGmailLogin(self):
        emailId = "email_address"
        passW = "password"
        
        print("")
        print("clicking on 'Got It'...")
        self.driver.find_element_by_id("com.google.android.gm:id/welcome_tour_got_it").click()

        print("clicking on 'Add an email address'...")
        self.driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another").click()
        
        
        print("clicking on 'Google'...")
        self.driver.find_element_by_id("com.google.android.gm:id/account_setup_item").click()
        print("loading")
        sleep(15)
        
        emailTF = self.driver.find_element_by_id("identifierId")
        print("entering email...")
        emailTF.send_keys(emailId)
        sleep(2)
        
        self.driver.find_element_by_id("identifierNext").click()

        pwdTF = self.driver.find_element_by_class_name("android.widget.EditText")
        print("entering password...")
        pwdTF.send_keys(passW)
        
        
        print("logging in...")
        self.driver.find_element_by_id("passwordNext").click()
        sleep(1)
        
        
        profile = self.driver.find_element_by_id("profileIdentifier")
        
        self.assertEqual(profile.get_attribute("name"), emailId)
        print("you're now logged in with " + emailId + "...")
        self.driver.find_element_by_id("signinconsentNext").click()
        
        sleep(10)
        
        
        self.driver.find_element_by_id("com.google.android.gms:id/next_button").click()
        sleep(1)
        
        print("clicking on 'TAKE ME TO GMAIL'...")
        self.driver.find_element_by_id("com.google.android.gm:id/action_done").click()
        sleep(40)
        
        print("logging out...")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        
        self.driver.find_element_by_id("com.google.android.gm:id/account_list_button").click()
        
        self.driver.find_element_by_id("com.google.android.gm:id/manage_accounts_text").click()
        
        content = self.driver.find_elements_by_class_name("android.widget.TextView")
        for x in content:
            if x.text == emailId:
                x.click()
                break
        
        self.driver.find_element_by_id("com.android.settings:id/button").click()
        
        self.driver.find_element_by_id("android:id/button1").click()
        
        print("you're now logged out...")
        sleep(5)
    
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GmailTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


#driver.find_element_by_id("com.google.android.gm:id/welcome_tour_skip").click()
#time.sleep(2)
#driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another").click()
#time.sleep(2)
#driver.find_element_by_id("com.google.android.gm:id/account_setup_item").click()
#time.sleep(10)

#driver.find_element_by_id("com.google.android.gms:id/identifierId").send_keys("undefeated0527")
#time.sleep(5)

#if self.driver.find_element_by_id("com.google.android.gms:id/identifierId").text == "undefeated0527":
#print("passed")
#else:
#print("failed")




