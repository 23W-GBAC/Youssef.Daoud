import psutil
from plyer import notification
import time

class ComputerUsageTracker:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = time.time()

    def track_computer_usage(self):
        while True:
            # Get the total system uptime
            uptime = time.time() - self.start_time

            # Check if the user has exceeded the time limit
            if uptime > self.time_limit:
                self.notify_user()

            # Check computer usage every 60 seconds (adjust as needed)
            time.sleep(60)

    def notify_user(self):
        notification_title = "Computer Usage Alert"
        notification_message = f"You have exceeded the set time limit of {self.time_limit / 60} minutes!"
        
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name="Computer Usage Tracker",
            timeout=10  # Display the notification for 12 seconds
        )
        
if __name__ == "__main__":
    # Set the time limit in seconds (adjust as needed)
    time_limit_seconds = 3600  # 1 hour

    # Create an instance of the ComputerUsageTracker
    tracker = ComputerUsageTracker(time_limit_seconds)

    # Start tracking computer usage
    tracker.track_computer_usage()
