from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os.path

lines = []
print('Hit Enter to start downloading song(s).')
while True:
    line = input('Enter song to be downloaded: ')
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
song_list = text.split('\n')

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
            return true;
        """)
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def get_song_url(driver, url):
    driver.get(url)
    return driver.find_element_by_xpath("//a[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']").get_attribute("href")
def convert_to_mp3(driver, url):
    driver.get('https://flvto.ch/')
    driver.find_element_by_tag_name('body').click()
    driver.find_element_by_xpath('//input[@id="convertUrl"]').send_keys(url)
    driver.find_element_by_xpath('//button[@id="yt-info"]').click()
    print('converting song to mp3...')
    while (not check_exists_by_xpath(driver, '//a[@class="button huge dark converter"]')):
        time.sleep(3)
def download(driver):
    driver.find_element_by_xpath('//a[@class="button huge dark converter"]').click()
    print('downloading...')
    time.sleep(60)

for song in song_list:
    song_name = song + " official song"
    url = "https://youtube.com/results?search_query=" + song_name.replace(' ', '+')
    try:
        print('Song to be downloaded: ' + song)
        options = Options()
        options.add_argument("--window-size=0,0")
        options.add_argument("--disable-notifications")
        # Edit the below line according to the folder you want to download the files into.
        options.add_experimental_option("prefs", {"download.default_directory": r"/Users/rishabhtatia/Documents/ishaq"})
        # Delete the line above if you want to download files in your default location.
        driver = webdriver.Chrome(chrome_options=options)
        driver.minimize_window()
        print('browser opened...')
        url = get_song_url(driver, url)
        print('got song url... ' + url)
        convert_to_mp3(driver, url)
        download(driver)
        print('song downloaded: ' + song)
        driver.quit()
        print('browser closed.')
    except Exception as e:
        print(e, '\nadding song to the end of the list.')
        song_list.append(song)
        # driver.quit()
