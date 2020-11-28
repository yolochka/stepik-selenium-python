from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Chrome()
	browser.get(link)
	WebDriverWait(browser,5).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
	browser.find_element_by_tag_name("button").click()
	x = browser.find_element_by_id("input_value").text
	browser.find_element_by_id("answer").send_keys(calc(x))
	browser.find_element_by_css_selector("[type='submit']").click()

finally:
	time.sleep(10);
	browser.quit();
