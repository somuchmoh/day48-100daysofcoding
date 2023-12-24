from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

events = driver.find_element(By.CLASS_NAME, "event-widget ul")
event_dict = {}

time_list = []
for time in events.find_elements(By.CSS_SELECTOR, "time"):
    time = time.text
    time_list.append(time)

name_list = []
for name in events.find_elements(By.CSS_SELECTOR, "a"):
    name = name.text
    name_list.append(name)

for i in range(0, len(time_list)):
    event_dict[i] = {"time": time_list[i], "name": name_list[i]}

print(event_dict)
driver.quit()