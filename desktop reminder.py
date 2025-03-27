import time
import pyttsx3
from plyer import notification

engine = pyttsx3.init()
REPEAT_INTERVAL = 5  # in seconds

while True:
    engine.say("Hey Sheetal, drink water!")
    engine.runAndWait()
    
    notification.notify(
        title="Hydration Reminder 💧",
        message="Hey Sheetal, time to drink some water!",
        timeout=5
    )

    time.sleep(REPEAT_INTERVAL)
