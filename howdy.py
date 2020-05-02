import webbrowser as wb
from pynput.keyboard import Key, Controller
import time

kb = Controller()
wb.open_new_tab('https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true')
time.sleep(2)
kb.type('tatiaris')
kb.press(Key.tab)
kb.press(Key.enter)
time.sleep(2)
# kb.type('Gottobe$&@18')
kb.press(Key.enter)
kb.press(Key.enter)