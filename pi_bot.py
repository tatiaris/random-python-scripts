import datetime
import os
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
gc_name = 'gang'

def open_app(name):
	os.system('open /Applications/' + name + '.app/')

def send_reminder(c_time):
	h, m = c_time.hour, c_time.minute
	r_h = 0
	if h == 15:
		if m <= 14:
			r_h = 0
		else:
			r_h = 12
	elif h == 3:
		if m <= 14:
			r_h = 0
		else:
			r_h = 12
	elif 15 > h > 3:
		r_h = 15 - h
	elif 0 <= h < 3:
		r_h = 3 - h
	else:
		r_h = 3 + (24 - h)

def find_gc(n):
	keyboard.press(Key.cmd)
	keyboard.press('f')
	keyboard.release(Key.cmd)
	time.sleep(1)
	keyboard.type(n)
	keyboard.press(Key.enter)
	time.sleep(2)

def send_messages(m, t):
	for i in range(t):
		keyboard.type(m)
		keyboard.press(Key.enter)
	time.sleep(60)
	os.system("pkill WhatsApp")

def check_time(h, m, txt):
	if ((currentDT.hour == h or currentDT.hour == h + 12) and currentDT.minute == m):
		open_app('WhatsApp')
		time.sleep(10)
		find_gc(gc_name)
		send_messages(txt, 1)

while True:
	currentDT = datetime.datetime.now()
    # checks if it's any of the times
	check_time(3, 14, 'pi')
	check_time(4, 20, '4:20')
	check_time(6, 28, 'tau')

	time.sleep(1)