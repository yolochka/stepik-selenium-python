from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_css_selector(".first_block .first").send_keys("FN")
	browser.find_element_by_css_selector(".first_block .second").send_keys("LN")	
	browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.ru")
	browser.find_element_by_tag_name("button").click()
	time.sleep(1)
	assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name("h1").text

finally:
	time.sleep(10)
	browser.quit()
	
	
