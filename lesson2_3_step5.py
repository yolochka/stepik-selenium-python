from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_tag_name("button").click()
	#browser.switch_to.alert.accept()
	browser.switch_to.window(browser.window_handles[1])
	
	x = browser.find_element_by_id("input_value").text
	browser.find_element_by_id("answer").send_keys(calc(x))
	browser.find_element_by_css_selector("[type='submit']").click()
	
	
finally:
	time.sleep(10)
	browser.quit()
	

