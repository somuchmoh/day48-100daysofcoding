from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# How to input something into the search bar?
fname = driver.find_element(By.NAME, "fName")
fname.click()
fname.send_keys("Mohana")

lname = driver.find_element(By.NAME, "lName")
lname.click()
lname.send_keys("Madhurakavi")

email = driver.find_element(By.NAME, "email")
email.click()
email.send_keys("mohana@text.io")

# You can also use the link text selector to click on a link with a particular text in it.
# click_link = driver.find_element(By.LINK_TEXT, "Content portals")
# click_link.click()

# You can use .click() method to click on a link/button in Selenium
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

# Getting Selenium to press 'ENTER' key
# search.send_keys(Keys.ENTER)


