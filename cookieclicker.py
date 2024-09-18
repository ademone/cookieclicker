from selenium import webdriver
from selenium.webdriver.common.by import By


# Keeep browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_find = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
while True:
    cookie_find.click()
