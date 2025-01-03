import time
import requests
from plyer import notification

# Constants
API_URL = "https://v2.twinoaksadvantage.com/tosdapi/api/MemberInformation/GetCrowdLevel"
THRESHOLD = 0.20
CHECK_INTERVAL = 300 
COOLDOWN = 3600
headers = {
    "API_KEY": "521DDB26-7EEE-4149-9193-539E720F9D48"
}
params = {
    "clubId": 3131
}

def check_crowd_level():
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data < THRESHOLD:
            print("Crowd level is below threshold. Notifying user.")
            notification.notify(
            title="Gym Crowd Level Alert",
            message=f"The crowd level is now {data}. It's a good time to go!",
            timeout=10
        )
            return True
        else: 
            return False
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        print("Response:", response.text)
        return False

def main():
    """Main function to check the crowd level periodically."""
    while True:
        if check_crowd_level():
            time.sleep(COOLDOWN)
        else:
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()