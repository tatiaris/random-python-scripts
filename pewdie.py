from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def convert_to_mp3(driver, url):
    driver.get('https://www.flvto.biz/')
    driver.find_element_by_tag_name('body').click()
    driver.find_element_by_xpath('//div[@class="checkbox__checkmark checkbox__checkmark_margin"]').click()
    driver.find_element_by_xpath('//input[@name="url"]').send_keys(url)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.find_element_by_tag_name('body').click()
    print('converting song to mp3...')
    while driver.current_url == "https://www.flvto.biz/fr/":
        time.sleep(3)

def new_account(name):
    print('generate name')

def download(driver):
    driver.get(driver.find_element_by_xpath('//a[@class="button huge track"]').get_attribute('href'))

def enter_first_page_info(driver, fname, lname, username, pw):
    driver.find_element_by_xpath('//input[@id="firstName"]').send_keys(fname)
    driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(lname)
    driver.find_element_by_xpath('//input[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//input[@name="Passwd"]').send_keys(pw)
    driver.find_element_by_xpath('//input[@name="ConfirmPasswd"]').send_keys(pw)

try:
    options = Options()
    # options.add_argument("--window-size=0,0")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    # driver.minimize_window()
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
    enter_first_page_info(driver, 'rishabh', 'tatia', 'rt101010', 'pw23423323')
    # driver.quit()
except Exception as e:
    print(e)
