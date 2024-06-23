from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="***********take rest*************",
            message="Rest is better for our health. It makes us stress-free.",
            app_icon="C:/Users/ashut/Downloads/sleep.ico",  # Ensure the icon file is correct
            timeout=10
        )
        time.sleep(10)

 