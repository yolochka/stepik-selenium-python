import os
from selenium import webdriver
import time


link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_name("firstname").send_keys("FN")
	browser.find_element_by_name("lastname").send_keys("LN")
	browser.find_element_by_name("email").send_keys("f@l.ru")
	current_dir = os.path.abspath(os.path.dirname("lesson2_2_step7.py"))
	print(current_dir)
	file_path = os.path.join(current_dir, 'file.txt')
	browser.find_element_by_name("file").send_keys(file_path)

	browser.find_element_by_tag_name("button").click()
	
finally:
	time.sleep(10)
	browser.quit()

