import time
from plyer import notification  
   
   
   
while True:
    notification.notify(title = "Reminder!", message = "You need to drink some water ",)
    time.sleep(60*60)