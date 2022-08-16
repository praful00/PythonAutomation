import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#headmode = bydeafault browser open in headmode
#headless = run script without opening the browser

#chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
#chrome_options.add_argument("--ignore-certificate-error") its handle site when site on safe mode


s = Service('C:\\Users\\pro\\PycharmProjects\\pro\\venv\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame('courses-iframe')
action = ActionChains(driver)
m = driver.find_element(By.LINK_TEXT, "More")
action.move_to_element(m).perform()
time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Contact")).click().perform()

#default content is use to out of the frame
driver.switch_to.default_content()
driver.find_element(By.ID, "autocomplete").send_keys("praful")