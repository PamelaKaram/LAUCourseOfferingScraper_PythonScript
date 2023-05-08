import sys 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



if len(sys.argv) < 3:
    print("Please provide both username and password as command-line arguments")
    sys.exit()

username = sys.argv[1]
password = sys.argv[2]

# Set up service for Chrome driver
service = Service(executable_path="../chromedriver.exe")

# Set binary location for Chrome
chr_options = webdriver.ChromeOptions()
chr_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# Go to website
driver = webdriver.Chrome(executable_path="../chromedriver.exe", chrome_options=chr_options)
driver.get("https://myportal.lau.edu.lb/")
#enter username and password and click enter
driver.find_element("name", "username").send_keys(username)  
driver.find_element("name", "password").send_keys(password)
driver.find_element("xpath", "//input[@type='submit' and @value='Log In']").send_keys(Keys.ENTER)


