from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# --------- Log In Values
USER_NAME = "your_email"
PASSWORD = "your_pass"

# --------- Selenium & Chrome Executing
chrome_path = "..//PycharmProjects/chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_path))

# --------- Open Instagram On Chrome
driver.get("https://www.instagram.com")
sleep(2)

# --------- Log In And Wait For Loading
user_name = driver.find_element(By.NAME, value="username")
user_name.send_keys(USER_NAME)
password = driver.find_element(By.NAME, value="password")
password.send_keys(PASSWORD)
sign_in_button = driver.find_element(By.CLASS_NAME, value="L3NKy")
sign_in_button.click()
sleep(6)

# --------- Search And Find Followers
to_search = "aliexpress"
search_bar = driver.find_element(By.CLASS_NAME, value="d_djL ")
search_bar.send_keys(to_search)
sleep(1)
search_bar.send_keys(Keys.ENTER)
result_tag = driver.find_element(By.CLASS_NAME, value="uL8Hv    ")
result_tag.click()
sleep(5)
open_followers_popup = driver.find_element(By.CSS_SELECTOR, value=".Y8-fY a")
open_followers_popup.click()
sleep(2)

# --------- Send Request To All Followers
followers_popup = driver.find_element(By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
    sleep(2)
follow_buttons = driver.find_elements(By.CSS_SELECTOR, value="button.y3zKF")

for buttons in follow_buttons:
    sleep(15)
    buttons.click()
    
# You will be blocked for a while in minutes by Instagram anyway :)
