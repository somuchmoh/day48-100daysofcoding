from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps Chrome browser open after program finishes running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.imagineonline.store/products/airpods-pro-mlwk3hn-a")
driver.quit()

price = driver.find_element(By.CLASS_NAME, "money").text
print(price)


