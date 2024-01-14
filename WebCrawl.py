#1-13-24 
# This program is still a work in progress but the idea behind it is to automate scanning the inter-webs for a expression that matches ip addresses, and to download any files that may meet those requirements
#
import subprocess
import random
import time

def generate_random_ip():
    # Generate a random IP address
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def download_files_with_ip_pattern(ip_address):
    # Use wget to download files matching the IP address pattern
    wget_command = f'wget --recursive --no-clobber --no-parent --accept-regex="{ip_address}" http://{ip_address}'
    subprocess.run(wget_command, shell=True)

def main():
    # Run the program indefinitely
    while True:
        # Generate a random IP address
        random_ip = generate_random_ip()

        # Download files with the random IP address pattern
        download_files_with_ip_pattern(random_ip)

        # Wait for some time before the next iteration
        time.sleep(60)  # Adjust the time interval as needed

if __name__ == "__main__":
    main()
