from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

link = "http://suninjuly.github.io/selects2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	num1 = int(browser.find_element_by_id("num1").text)
	num2 = int(browser.find_element_by_id("num2").text)
	sum_num = str(num1 +num2)
	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_value(sum_num)
	browser.find_element_by_css_selector("[type='submit']").click()
	
finally:
	time.sleep(10)
	browser.quit()
	
	
	
