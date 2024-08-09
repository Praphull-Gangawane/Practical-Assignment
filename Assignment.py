from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the browser and navigate to the login page
driver.get("https://dev.smartodr.in/login")

# Enter the username and password
driver.find_element(By.ID, "email").send_keys("your_email")
driver.find_element(By.ID, "password").send_keys("your_password")

# Click on the login button
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/form/button").click()

# Verify login success
assert "Logout" in driver.page_source

# Close the browser
driver.quit()
