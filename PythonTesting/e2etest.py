import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
time.sleep(3)
for product in products:
    productname = product.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successmsg = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you! " in successmsg
