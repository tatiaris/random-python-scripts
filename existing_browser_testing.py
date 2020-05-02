from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def start_typing(passage):
    p_list = passage.split(' ')
    pg.typewrite(passage)

driver = webdriver.Chrome()
driver.get('https://www.typeracer.com/')
pg.hotkey('ctrl', 'alt', 'i')
passage = ''
while True:
    time.sleep(1)
    try:
        tr_str = str(driver.find_elements_by_xpath('//span[@class="time"]')[1].text[0:])
        tr = int(tr_str[tr_str.find(':') + 1:])
    except:
        tr = 100
    if tr < 6:
        passage_parts = driver.find_elements_by_xpath('//span[@unselectable="on"]')
        for i in range(len(passage_parts)):
            if i == (len(passage_parts) - 1):
                passage += ' '
            passage += str(passage_parts[i].text)
        break

time.sleep(5.2)

start_typing(passage)