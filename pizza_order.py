from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def booler(s):
	if s[0] == 'n':
		return False
	else:
		return True

usual = booler(input("Use usual info? (Enter 'y' or 'n'): "))
pep = booler(input("Peperonni? (Enter 'y' or 'n'): "))

if not usual:
	address = input('Enter Street Adress: ')
	city = input('Enter City: ')
	state = input('Enter State: ')
	zip_code = input('Enter Zip Code: ')
	email = input('Enter Email: ')
	phone = input('Enter Phone number: ')
	f_name = input('Enter first name: ')
	l_name = input('Enter last name: ')
else:
	address = '25714 Creek Ledge Dr'
	city = 'Katy'
	state = 'tx'
	zip_code = '77494'
	email = 'rishabhtatia10104@gmail.com'
	phone = '2244108854'
	f_name = 'Rishabh'
	l_name = 'Tatia'

driver = webdriver.Chrome()
driver.get('https://www.dominos.com/en/')
time.sleep(2)
driver.find_element_by_xpath("//a[@data-method='Delivery']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='Street']").send_keys(address)
driver.find_element_by_xpath("//input[@id='City']").send_keys(city)
driver.find_element_by_xpath("//select[@id='Region']").send_keys(state)
driver.find_element_by_xpath("//input[@id='Postal_Code']").send_keys(zip_code)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
driver.find_element_by_xpath("//h2[@data-quid='entree-title-epic']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[@data-quid='pizza-size-12-size']").click()
driver.find_element_by_xpath("//a[@data-quid='pizza-builder-next-btn']").click()
driver.find_element_by_xpath("//a[@data-quid='pizza-builder-next-btn']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@data-quid='builder-no-step-upsell']").click()

if pep:
	driver.find_element_by_xpath("//input[@class='selectTopping js-Meat c-topping-P topping-P']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@data-quid='add-pizzabuilder-button']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@data-quid='pizza-sides-no-thanks']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@data-quid='order-checkout-button']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@data-quid='overlay-no-thanks']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@data-quid='continue-checkout-btn']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
driver.find_element_by_xpath("//input[@id='Callback_Phone']").send_keys(phone)
driver.find_element_by_xpath("//input[@id='First_Name']").send_keys(f_name)
driver.find_element_by_xpath("//input[@id='Last_Name']").send_keys(l_name)
driver.find_element_by_xpath("//input[@data-quid='payment-cash']").click()
# driver.find_element_by_xpath("//button[@data-quid='payment-order-now']").click()
# driver.quit()