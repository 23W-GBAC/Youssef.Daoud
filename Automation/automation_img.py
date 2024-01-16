import psutil
from plyer import notification
import time

class InternetUsageTracker:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = time.time()

    def track_internet_usage(self):
        while True:
            # Get the total system uptime
            uptime = time.time() - self.start_time

            # Check if the user has exceeded the time limit
            if uptime > self.time_limit:
                self.notify_user()

            # Check internet usage every 60 seconds (adjust as needed)
            time.sleep(60)

    def notify_user(self):
        notification_title = "Internet Usage Alert"
        notification_message = f"You have exceeded the set time limit of {self.time_limit / 60} minutes."
        
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name="Internet Usage Tracker",
            timeout=10  # Display the notification for 10 seconds
        )
        # You can add additional actions here, such as logging the violation or blocking internet access.

if __name__ == "__main__":
    # Set the time limit in seconds (adjust as needed)
    time_limit_seconds = 3600  # 1 hour

    # Create an instance of the InternetUsageTracker
    tracker = InternetUsageTracker(time_limit_seconds)

    # Start tracking internet usage
    tracker.track_internet_usage()
