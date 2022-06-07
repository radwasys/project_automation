from http.client import HTTPS_PORT
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chromediver_win32\ \(1\)/

repo_name = sys.argv[1]
print(f'hello {repo_name}')
PATH = "/mnt/c/Users/tokka/Downloads/chromedriver_win321/chromedriver.exe"
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(PATH)
driver.get('https://github.com/new')
time.sleep(5)
username_input = driver.find_element(By.ID, "login_field")
username_input.click()
username_input.send_keys("Radwasys")
password_input = driver.find_element(By.ID, "password")
password_input.click()
password_input.send_keys("drradwa2007")
password_input.send_keys(Keys.RETURN)
time.sleep(2)
repo_name_input = driver.find_element(By.ID, "repository_name")
repo_name_input.send_keys(repo_name)
readme_check = driver.find_element(By.ID, "repository_auto_init")
readme_check.click()
time.sleep(2)
submit_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
submit_btn.click()
print("Repository created!")

time.sleep(3)
code_btn = driver.find_element(By.CSS_SELECTOR, ".d-none.d-md-flex.ml-2")
code_btn.click()
http_btn = driver.find_element(
    By.CSS_SELECTOR, ".UnderlineNav-item.lh-default.f6.py-0.px-0.mr-2.position-relative")
http_btn.click()
http_link_btn = driver.find_element(
    By.CSS_SELECTOR, ".form-control.input-monospace.input-sm.color-bg-subtle")
http_link = http_link_btn.get_attribute("value")
print(f'http link: {http_link}')
