from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service('C:\\Users\\pro\\PycharmProjects\\pro\\venv\\chromedriver.exe')


driver=webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")
driver.maximize_window()
print("page title:", driver.title)




