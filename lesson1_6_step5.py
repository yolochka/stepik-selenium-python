import math 
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_link_text(link_text).click()
	browser.find_element_by_name("first_name").send_keys("Ivan")
	browser.find_element_by_name("last_name").send_keys("Petrov")
	browser.find_element_by_class_name("city").send_keys("Smolensk")
	browser.find_element_by_id("country").send_keys("Russia")
	browser.find_element_by_class_name("btn-default").click()
	
finally:
	time.sleep(10)
	browser.quit()	
	
