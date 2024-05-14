from selenium import webdriver
import time

# Set up Chrome driver
driver = webdriver.Chrome()

# Navigate to login page and enter credentials
driver.get("https://www.citilink.ru/login")
driver.find_element_by_name("username").send_keys("+79200800857")
driver.find_element_by_name("password").send_keys("WPWWPW0082024_08")
driver.find_element_by_name("submit").click()

# Wait for page to load after auth
time.sleep(2)

# Navigate to home page and print title
driver.get("https://www.citilink.ru/")
print(driver.find_element_by_xpath("//h1[@class='title']").text)

# Close browser
driver.quit()