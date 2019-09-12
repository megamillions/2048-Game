#! python3
# 2048.py - Bot that plays 2048 tile game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open browser to the game page.
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

# Introduce a counter for flavor.
counter = 0

# Trigger to continue or end play in while-loop later.
def CheckIfOver():

	try:
		return browser.find_element_by_css_selector('.game-over')

	except:
		return None

overElem = CheckIfOver()

# while-loop to play through the game.
while overElem is None:

	# Move in a clockwise direction, forever.
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)

	counter += 1

	# Decide whether to continue or end.
	overElem = CheckIfOver()

print("Congratulations! Victory in only %s turns." % str(counter))