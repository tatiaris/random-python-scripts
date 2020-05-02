from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# get song name as input from user
song_name = input('Enter song name: ').split(' ')

# generate url for lyrics website
url = 'http://www.songlyrics.com/index.php?section=search&searchW='
for i in range(len(song_name)-1):
    url += song_name[i] + '+'
url += song_name[-1] + '&submit=Search'

try:
    # open the browser window and minimize
    options = Options()
    options.add_argument("--window-size=0,0")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.minimize_window()
    driver.get(url)
    time.sleep(2)

    # click the first h3 element to get to the lyrics page
    lyrics_url = driver.find_element_by_xpath("//div[@class='serpresult']/a").get_attribute("href")
    driver.get(lyrics_url)
    while driver.current_url != lyrics_url:
        time.sleep(3)

    # get the lyrics text in a string
    elem = driver.find_element_by_xpath("//p[@id='songLyricsDiv']")
    lyrics_text = elem.text
    print('\nlyrics: \n' + lyrics_text + '\n')

except Exception as e:
    print(e)

driver.quit()
