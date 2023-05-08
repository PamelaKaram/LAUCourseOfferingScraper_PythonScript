import sys 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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