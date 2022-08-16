from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:\\Users\\pro\\PycharmProjects\\pro\\venv\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
item = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(item))

for itemlist in item:
    producrname=itemlist.find_element(By.XPATH, "div/h4/a").text
    if producrname =="Blackberry":
        itemlist.find_element(By.XPATH, "div/button").click()
        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
