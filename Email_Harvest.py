# this program is used as a email gathering tool trying to match regular expressions which can be set manually incase specific crawling is needed.
#
#
import requests
from bs4 import BeautifulSoup
import re

def crawl_for_emails(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all email addresses in the HTML content
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup))

        # Print or store the email addresses
        for email in email_addresses:
            print(email)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the URL you want to crawl for emails
    target_url = "https://example.com"

    # Call the function to crawl for emails
    crawl_for_emails(target_url)
