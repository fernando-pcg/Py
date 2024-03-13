from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://59727441-16-0-all.runbot185.odoo.com/web/login")

username = driver.find_element(By.ID, "login")
username.send_keys("admin")
password = driver.find_element(By.ID, "password")
password.send_keys("admin")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Go to sales module and create a quotation with a product and partner
driver.get("https://59727441-16-0-all.runbot185.odoo.com/web#action=1279&model=sale.order&view_type=list&cids=1&menu_id=874")

create_button = driver.find_element(By.XPATH )


driver.quit()