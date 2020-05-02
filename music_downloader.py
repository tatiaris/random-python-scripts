from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Music Downloader")
root.geometry("900x180+600+100")
Label(root, text="Songs to be downloaded:").grid(row=1, column=0)
user_input = ScrolledText(root, height=4); user_input.grid(row=1, column=1)

def get_song_list(all_songs):
    list = all_songs.split('\n')
    list = list[:-1]
    return list
def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
            return true;
        """)
def get_song_url(driver, url):
    driver.get(url)
    return driver.find_element_by_xpath("//a[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']").get_attribute("href")
def convert_to_mp3(driver, url):
    driver.get('https://www.flvto.biz/')
    driver.find_element_by_xpath('//div[@class="checkbox__checkmark checkbox__checkmark_margin"]').click()
    driver.find_element_by_xpath('//input[@name="url"]').send_keys(url)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.find_element_by_tag_name('body').click()
    print('converting song to mp3...')
    while driver.current_url == "https://www.flvto.biz/de/":
        time.sleep(3)
def download(driver):
    driver.get(driver.find_element_by_xpath('//a[@class="button huge track"]').get_attribute('href'))

def start_download():
    list = get_song_list(user_input.get(1.0, END))
    for song in list:
        song_name = song + " official song"
        url = "https://youtube.com/results?search_query=" + song_name.replace(' ', '+')
        try:
            print('Song to be downloaded: ' + song)
            options = Options()
            options.add_argument("--window-size=100,50")
            # Edit the below line according to the folder you want to download the files into.
            options.add_experimental_option("prefs", {"download.default_directory": r"/Users/rishabhtatia/Desktop/music/all_songs"})
            # Delete the line above if you want to download files in your default location.
            driver = webdriver.Chrome(chrome_options=options)
            print('browser opened...')
            url = get_song_url(driver, url)
            print('got song url... ' + url)
            convert_to_mp3(driver, url)
            download(driver)
            print('downloading...')
            driver.get('chrome://downloads/')
            while not every_downloads_chrome(driver):
                time.sleep(3)
            print('song downloaded: ' + song)
            driver.quit()
            print('browser closed.')
            print('\n')
        except Exception as e:
            print(e)
            driver.quit()



submit = Button(root, text = "Submit", width = 30, height = 2, bg = 'lightblue', command = start_download).place(x = 250, y = 90)
root.mainloop()
