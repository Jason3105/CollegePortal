import time
import requests

URL = "https://collegeportal-yake.onrender.com"

def keep_awake():
    while True:
        try:
            response = requests.get(URL)
            print(f"Pinged {URL} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error pinging {URL}: {e}")

        # Wait for 10 minutes before the next ping
        time.sleep(600)  # 600 seconds = 10 minutes

if __name__ == "__main__":
    keep_awake()
