from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r"C:\\Users\\Umka\PycharmProjects\Selenium\firefoxdriver\geckodriver.exe")

url1 = 'https://www.google.com'
url2 = 'https://vk.com/'

username = '87754521515'
password = 'umkaggwpggwp'

# Task 1:
# try:
#     driver.get(url=url1)
#     time.sleep(2)
#     searchInput = driver.find_element(By.CSS_SELECTOR, "input[name=q]")
#     searchInput.send_keys("Hello World!")
#     time.sleep(2)
#     searchBtn = driver.find_element(By.XPATH, "//input[@name='btnK']")
#     searchBtn.click()
#     time.sleep(2)
#     print('Test 1 passed!')
# except Exception as ex:
#     print(ex)
#     print('Test 1 failed!')
# finally:
#     driver.close()
#     driver.quit()

# Task 2:
try:
    driver.get(url=url2)
    driver.maximize_window()
    time.sleep(2)
    # Log In
    signInInput = driver.find_element(By.XPATH, '//*[@id="index_email"]')
    signInInput.click()
    signInInput.send_keys(username)
    signInButton = driver.find_element(By.CSS_SELECTOR, 'button.FlatButton:nth-child(5) > span:nth-child(1)')
    signInButton.click()
    time.sleep(3)
    passwordInput = driver.find_element(By.NAME, 'password')
    passwordInput.click()
    passwordInput.send_keys(password)
    time.sleep(3)
    passwordButton = driver.find_element(By.CLASS_NAME, 'vkuiButton__in')
    passwordButton.click()
    time.sleep(10)
    # Log Out
    menuBtn = driver.find_element(By.XPATH, '//*[@id="top_profile_link"]')
    menuBtn.click()
    time.sleep(2)
    LogoutButton = driver.find_element(By.CSS_SELECTOR, '#top_logout_link')
    LogoutButton.click()
    time.sleep(3)
    print('Test 2 passed!')
except Exception as ex:
    print(ex)
    print('Test 2 failed!')
finally:
    driver.close()
    driver.quit()
