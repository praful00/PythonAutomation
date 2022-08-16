import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:\\Users\\pro\\PycharmProjects\\pro\\venv\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,1000)")

time.sleep(2)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")