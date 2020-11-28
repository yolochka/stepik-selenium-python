from selenium import webdriver
import time

link = link = "http://suninjuly.github.io/huge_form.html"
try:
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(link)
	elements = browser.find_elements_by_css_selector('input[type="text"]')
	for element in elements:
		element.send_keys("1")
	browser.find_element_by_class_name("btn-default").click()
	
finally:
	time.sleep(10)
	alert=browser.switch_to_alert()
	print(alert.text)
	time.sleep(10)
	browser.quit()
	
