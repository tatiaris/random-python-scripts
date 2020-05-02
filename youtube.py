from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

search_query = input()
url = 'https://youtube.com/results?search_query=' + search_query.replace(' ', '+')

try:
    driver = webdriver.Chrome()
    driver.get(url)
    trailer_link = driver.find_element_by_xpath("//a[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']").get_attribute("href")
    time.sleep(3)
    vid_length = driver.find_element_by_xpath("//span[@class='style-scope ytd-thumbnail-overlay-time-status-renderer']").get_attribute('innerHTML').replace(' ', '').replace("\n", '')
    total_seconds = (int(vid_length[0:vid_length.find(':')])*60) + int(vid_length[vid_length.find(':')+1:len(vid_length)])
    driver.get(trailer_link)
    time.sleep(2)
    driver.find_element_by_tag_name('body').send_keys('f')
    time.sleep(total_seconds + 5)
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()
