from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\Development\chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


driver.get("https://www.python.org/")

times = driver.find_elements(
    By.CSS_SELECTOR,
    value='.event-widget time'
)

titles = driver.find_elements(
    By.CSS_SELECTOR,
    value='.event-widget .menu a'
)

events = {}
for i in range(len(times)):
    new = {
            'time': times[i].text,
            'event': titles[i].text
            }

    events[i] = new

print(events)


driver.quit()