import psutil
from plyer import notification
import time

def is_laptop_open():
    try:
        # Get information about battery status
        battery = psutil.sensors_battery()
        if battery:
            # Check if the lid is open (True) or closed (False)
            return battery.power_plugged or battery.percent > 95
    except Exception as e:
        print(f"Error checking laptop status: {e}")
    return True  # Default to considering the laptop as open

def notify_alert():
    notification.notify(
        title="Laptop Alert",
        message="Your laptop has been opened!",
        app_name="Laptop Monitor",
    )

def main():
    # Check the laptop status every 5 seconds
    while True:
        if not is_laptop_open():
            notify_alert()
            # Wait for 1 minute before checking again to avoid repeated notifications
            time.sleep(60)
        else:
            time.sleep(5)

if __name__ == "__main__":
    main()
