from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

#gets the current date and time to name the picture taken
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H.%M.%S")

camera.start_preview()
sleep(5)
camera.capture('/home/james/Desktop/CS2210/FINAL_PROJECT/' + dt_string + '.jpg')
camera.stop_preview()
