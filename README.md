# LAUCourseOfferingScraper_PythonScript
A python script that takes LAU  username and password as arguments. The script generates a well-formatted CSV file with details (Time, Instructor Name, Remaining Seats, etc.) about the upcoming Fall 2023 course offerings for the CS department at Byblos campus


## Introduction
This script uses the Selenium package to automate the process of looking up classes and extracting data from the LAU course registration system. The script logs in to the LAU portal, navigates to the class lookup page, selects the desired term and filters for specific subject and campus, then extracts the class data from the resulting table and saves it to a CSV file.

## Installation
To use this script, you need to install the following:

Python (version 3.7 or higher)
Selenium (Python package for automating web browsers)
ChromeDriver (the WebDriver for Chrome)

You can install Selenium and other packages by running pip install in your command prompt or terminal. 
To install ChromeDriver, download the appropriate version from the official website and add its executable path to the system path.
https://chromedriver.chromium.org/downloads

## Usage
To run the script, open your terminal or command prompt, navigate to the directory containing the script, and run the following command: python script.py username password

## How It Works
The script starts by importing the necessary packages and checking the command-line arguments for the username and password. Then, it sets up the Chrome driver service and binary options to launch the browser. The script navigates to the LAU portal login page and enters the credentials, logs in, and navigates to the course lookup page.

Once on the course lookup page, the script selects the desired term, then filters the results by subject and campus. It then extracts the data from the resulting table and saves it to a CSV file.

The script uses XPATH to locate elements in the HTML structure of the page and interacts with them using the send_keys() and click() methods. It also uses the Select class to interact with dropdown menus.

## Challenges Encountered
One common issue with web scraping is handling dynamic elements and waiting for the page to load. This script uses the WebDriverWait class from the selenium.webdriver.support.ui module to wait for specific elements to appear before interacting with them.

Another challenge encountered is dealing with nested tables, which can be tricky to parse correctly. This script uses XPATH to select specific rows and columns within the table and writes them to the CSV file.

## Final Notes
This script provides a useful tool for automating the process of searching for LAU courses. With the help of Selenium, users can quickly and easily navigate the LAU registration system and save the results to a CSV file.
