import sys 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



if len(sys.argv) < 3:
    print("Please provide both username and password as command-line arguments")
    sys.exit()

username = sys.argv[1]
password = sys.argv[2]

# Set up service for Chrome driver
service = Service(executable_path="../chromedriver.exe")

# Set binary location for Chrome
options = webdriver.ChromeOptions()
options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# Go to website
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://myportal.lau.edu.lb/")
#enter username and password and click enter
driver.find_element("name", "username").send_keys(username)  
driver.find_element("name", "password").send_keys(password)
driver.find_element("xpath", "//input[@type='submit' and @value='Log In']").send_keys(Keys.ENTER)

# Go to courses page
driver.find_element("xpath", '//a[@class="static menu-item" and @href="/sites/courses"]')\
    .send_keys(Keys.ENTER)

# Go to registration page
driver.find_element("xpath", '//a[@href="https://banweb.lau.edu.lb/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu"]')\
       .send_keys(Keys.ENTER)

# Switch to the new window
handles = driver.window_handles
new_win_handle = handles[-1]
driver.switch_to.window(new_win_handle)

# Go to class lookup page
driver.find_element("xpath", '//a[contains(text(), "Look-up Classes to Add")]')\
       .send_keys(Keys.ENTER)

# Select term from dropdown
select_element = driver.find_element("id", "term_input_id")
select = Select(select_element)
select.select_by_value("202410")

# Submit form
driver.find_element("xpath", "//input[@type='submit' and @value='Submit']")\
       .send_keys(Keys.ENTER)