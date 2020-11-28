import math
from selenium import webdriver
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
link = "http://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x = browser.find_element_by_id("input_value").text
	browser.find_element_by_id("answer").send_keys(calc(x))
	browser.find_element_by_id("robotCheckbox").click()
	browser.find_element_by_id("robotsRule").click()
	browser.find_element_by_css_selector("[type='submit']").click()
	
finally:
	time.sleep(10)
	browser.quit()

