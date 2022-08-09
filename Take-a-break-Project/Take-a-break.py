import time
from plyer import notification

if __name__ == "__main__":
    while True:
     notification.notify(
        title = "Take a break Champ",
        message = "According to experts, staring at screen for long time is not healthy for your eyes",
        app_icon = "C:\\Users\\mahan\\OneDrive\\Desktop\\PWH Python Notes 2\\Projects\\icon.ico",
        timeout=5
     )
     time.sleep(60*60)