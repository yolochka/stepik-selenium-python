from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	browser.find_element_by_name("first_name").send_keys("Ivan")
	browser.find_element_by_name("last_name").send_keys("Petrov")
	browser.find_element_by_class_name("city").send_keys("Smolensk")
	browser.find_element_by_id("country").send_keys("Russia")
	browser.find_element_by_id("submit_button").click()

finally:
	time.sleep(20)
	browser.quit()
	

