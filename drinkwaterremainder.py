import time
from plyer import notification

def water_reminder(interval_minutes):
    while True:
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink water!",
            app_icon=None,  # e.g., 'path/to/icon.png'
            timeout=10,  # seconds
        )

if __name__ == "__main__":
    interval_minutes = 30  # Set your desired reminder interval in minutes
    water_reminder(interval_minutes)
