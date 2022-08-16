from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://yuvicare.com:8080/YUVICARETEST/")
driver.maximize_window()
print("page title:",driver.title)
print("page url:",driver.current_url)
driver.find_element(By.ID,"email").send_keys("balgopal")
driver.find_element(By.NAME,"password").send_keys("Expert#100")
driver.find_element(By.ID,"lgnbtn").click()

driver.get("https://www.amazon.in/")
driver.back()
driver.forward()
