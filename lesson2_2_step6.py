from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x = browser.find_element_by_id("input_value").text

	
	browser.find_element_by_id("answer").send_keys(calc(x))
	browser.find_element_by_id("robotCheckbox").click()
	robotsRadio = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRadio)
	robotsRadio.click()
	browser.find_element_by_css_selector("[type='submit']").click()

finally:
	time.sleep(5)
	browser.quit()
