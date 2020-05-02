from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

def log_howdy(user_name, pw):
    driver.get('https://howdy.tamu.edu/')
    # driver.find_element_by_xpath('//input[@type="email"]').send_keys(user_name)
    # driver.find_element_by_xpath('//input[@type="password"]').send_keys(pw)
    # driver.find_element_by_xpath('//button[@class="signin-button full-width zb-button primary raised ember-view"]').click()
    time.sleep(3)

user_name = 'tatiaris'
pw = 'Gottobe$&@19'

prof = input('Enter professor name: ')

driver = webdriver.Chrome()
log_howdy(user_name, pw)

# driver.quit()
