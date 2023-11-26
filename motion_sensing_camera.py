from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import MotionSensor

camera = PiCamera()
pir = MotionSensor(4) #the PIR Sensor is connected to GPIO 4

# gets the current date and time to give each image a
# unique name. avoids overwriting images, and gives the
# user information about when the image was taken
pir.wait_for_motion()
camera.start_preview()
sleep(0.5)

dt_string = datetime.now().strftime('%d_%m_%Y_%H.%M.%S')
filename1 = ('/home/james/Desktop/CS2210/FINAL_PROJECT/images/' + dt_string + '1.jpeg')
camera.capture(filename1)
print("Image Captured") #line to make sure the motion sensing is working

sleep(0.5)
dt_string = datetime.now().strftime('%d_%m_%Y_%H.%M.%S')
filename2 = ('/home/james/Desktop/CS2210/FINAL_PROJECT/images/' + dt_string + '2.jpeg')
camera.capture(filename2)
print("Image Captured")

sleep(0.5)
dt_string_3 = datetime.now().strftime('%d_%m_%Y_%H.%M.%S')
filename3 = ('/home/james/Desktop/CS2210/FINAL_PROJECT/images/' + dt_string + '3.jpeg')
camera.capture(filename3)
print("Image Captured")
camera.stop_preview()
