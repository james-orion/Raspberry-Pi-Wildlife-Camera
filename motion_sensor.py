# Code taken from projects.raspberrypi.org/en/projects/parent-detector/3
from gpiozero import MotionSensor

pir = MotionSensor(4)

while(True):
    pir.wait_for_motion()
    print("Motion detected!")
    pir.wait_for_no_motion()
