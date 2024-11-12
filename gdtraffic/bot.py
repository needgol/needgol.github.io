!/usr/bin/env python

import webbrowser
import time
x = 1
while True:
  webbrowser.open('http://url/')
  time.sleep(15)
	webbrowser.open_new_tab('https://needgol.github.io/')
	time.sleep(15)
	webbrowser.open_new_tab('https://needgol.github.io/page/')
	time.sleep(20)	
	webbrowser.open_new_tab('https://needgol.github.io/mastersurf.html')
	time.sleep(45)
	webbrowser.open_new_tab('https://needgol.github.io/link-me/')
	time.sleep(120)	
	webbrowser.open_new_tab('https://needgol.github.io/link-me/')
	time.sleep(120)
	x +=1
