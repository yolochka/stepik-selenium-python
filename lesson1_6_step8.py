from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)	
	browser.get(link)
	
	browser.find_element_by_name("first_name").send_keys("1")
	browser.find_element_by_name("last_name").send_keys("1")
	browser.find_element_by_class_name("city").send_keys("1")
	browser.find_element_by_id("country").send_keys("1`")
	browser.find_element_by_xpath("//div//button[contains(text(),'Submit')").click()

finally:
	time.sleep(5)
	alert=browser.switch_to_alert()
	print(alert.text)
	time.sleep(5)
	browser.quit()
	

