# Raspberry-Pi-Wildlife-Camera

Introduction:
This project is intended to be a simple motion detecting camera that can be used to detect and capture wildlife or pets in the vicinity of the user. The motion detector has a range of approximately 20 feet, allowing the camera to capture images from fairly far away. When the motion detector detects movement from a living body (human or animal generally), it triggers the camera to take a number of pictures, hopefully capturing the creature moving around. 
Once the pictures are taken, the raspberry pi uploads them to a website, and sends a message to the user, indicating that they should go view their new pictures and see the wildlife the camera has captured. 

Key Definitions: 
•	PIR sensor: a passive infrared sensor, it senses changes in the infrared radiation that something gives off. In practice, they detect movement of humans and other animals in front of the sensor because they give off a high amount of infrared radiation. They are especially good at detecting warm blooded animals because the more heat something gives off, the higher its infrared radiation. 
•	GPIO: general purpose input/output. Pins on the raspberry pi that communicate with circuits and other incoming and outcoming digital signals. They can be set to either act as input or output depending on the needs for the project.
•	VCC: Voltage Common Collector, the power input for the device. In this case, the PIR sensor connects to the voltage from the Raspberry Pi through its VCC pin. 
•	GND: Ground. Grounding allows for electrical discharge from a circuit, avoiding the dangerous possibility of electricity building up within the wires or circuit.  

Project Description: 
The Raspberry Pi camera is designed to plug into the camera port on the Raspberry Pi 4. It comes with a connecting cable, and should just plug right into the port, allowing the pi to communicate with the camera.
We are planning to purchase a portable power bank so that the Raspberry Pi can be used outside, and otherwise not constrained by outlet placement in a particular area. This will just be a standard USB-C power bank that connects to the pi and acts as a power source very similar to the power cable that the pi came with. This ended up not happening because the power bank was out of stock when ordering parts, and it was decided that it was not a critical piece of the design. In the future if expanding on this project it would be worth including, but for the scope of this project it was not a priority. 
The PIR sensor comes with three pins that are used to attach to and connect it to the Raspberry Pi. As shown in the following diagram, those pins are all connected to different pins on the Raspberry Pi’s pin board. On the sensor, those pins are the DATA or OUT representing the output or data information that comes from the sensor and will be handled by the pi, this is connected to any of the GPIO pins, in the diagram it is connected to pin GPIO 21. The VCC pins connect the sensor to one of the voltage pins on the Raspberry Pi, and the GND pin connects to one of the ground pins on the Raspberry Pi board, allowing a complete circuit between the sensor and the pi. 
 
The code for this project will primarily be written in python, and will take in the data from the sensor, and when it senses motion, the code will then call functions that will then take a number of pictures, with a delay 0.5 seconds between each picture to capture the movement. The pi will then upload these images to a local web server hosted on the pi, and will notify the user of the captured images through email. This will use the Pi camera’s web interface module, which allows for a lot of functionality, including downloading images, deleting and saving, and can assist in triggering the image capture based on input from the motion sensor. This module will be extremely useful for this project, because it is designed to do a lot of the things that this wildlife camera is also designed to do. For the project I ended up not using this module because it had too many features that got in the way of the fairly simple design of the project. I spent a while trying to get it set up, but in the end it was a lot easier to just have the python script trigger the camera, and write a separate script that emailed the user when images were captured.

Final Reflection:
This project was definitely a challenge in time management and getting myself to take time to work on the project. I ended up leaving a lot of it until the end, which ended up being a challenge when right after getting the project working, my camera broke, and I ended up having to order a replacement part. Thankfully it came quickly and I was able to get it all fixed and working quickly and easily, but it would have been way better if this issue had happened earlier in the project process. Working alone meant that there was no one else to check in and motivate me to get my work done, which meant that I often would prioritize other work over this class because that work had more immediate due dates. 
Working alone also meant that all of the project ended up being on my plate which was alright, and it was nice to not have to deal with coordinating with group members but I also ended up responsible for each piece of it. It would have been nice to have a partner where one of us could have done the project manager role and the other could have taken on the lead programmer role. 
I am excited to work more with my raspberry pi, and to have it and the knowledge of it to just mess around and make cool stuff with it when I have the chance without the stress of deadlines and course projects. Overall I did enjoy the project, despite all of the stress of the last few weeks it was really cool to have a project at the end that did what I intended it to do, and that I had built basically completely from scratch. 

Works Cited: 
* 9. API - The PiCamera Class — Picamera 1.13 Documentation. (n.d.). https://picamera.readthedocs.io/en/release-1.13/api_camera.html
* Admin. (2021, August 23). How does electrical grounding work? OneMonroe. https://monroeengineering.com/blog/how-does-electrical-grounding-work/#:~:text=Grounding%20works%20by%20leveraging%20the,to%20discharge%20through%20the%20ground.
* BC Robotics Inc. (2022, June 14). Sending an email using Python on the Raspberry Pi - BC Robotics. BC Robotics. https://bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/
* Circuit Diagram - a circuit diagram maker. (n.d.). https://www.circuit-diagram.org/
* Flask loop through images in static directory. (n.d.). Stack Overflow. https://stackoverflow.com/questions/47378820/flask-loop-through-images-in-static-directory
* GeeksforGeeks. (2019, May 20). Python  os.listdir  method. https://www.geeksforgeeks.org/python-os-listdir-method/
* GeeksforGeeks. (2022, May 30). Retrieving  HTML Form data using Flask. https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
* Get Started with Pi Camera V2. (n.d.). Little Bird Electronics Guide. https://littlebirdelectronics.com.au/guides/198/get-started-with-pi-camera-v2
* Hattersley, R. (2021, September 18). Watch wildlife with a Raspberry Pi nature camera| Hackspace 33. Raspberry Pi. https://www.raspberrypi.com/news/watch-wildlife-with-a-raspberry-pi-nature-camera-hackspace-33/
* Help me to understand the two potmeters on my PIR sensor. (2016, March 16). Arduino Forum. https://forum.arduino.cc/t/help-me-to-understand-the-two-potmeters-on-my-pir-sensor/372895
* How to get current date and time in Python? (With Examples). (n.d.). https://www.programiz.com/python-programming/datetime/current-datetime
* How to kill a process that says “Operation not permitted” when attempted? (n.d.). Unix & Linux Stack Exchange. https://unix.stackexchange.com/questions/89316/how-to-kill-a-process-that-says-operation-not-permitted-when-attempted
* How to Receive Emails with the Flask Framework for Python. (n.d.). Sendgrid. https://sendgrid.com/en-us/blog/how-to-receive-emails-with-the-flask-framework-for-python
* How to save file on users local directory instead of server in flask? (n.d.). Stack Overflow. https://stackoverflow.com/questions/58782617/how-to-save-file-on-users-local-directory-instead-of-server-in-flask
* PIR Motion Sensor. (2014, January 28). Adafruit Learning System. https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview
* Problem recording video using Pi Camera v2 - Raspberry Pi Forums. (n.d.). https://forums.raspberrypi.com/viewtopic.php?t=210726
* Put all images from directory into HTML. (n.d.). Stack Overflow. https://stackoverflow.com/questions/33588691/put-all-images-from-directory-into-html
* raspberrypi.org. (n.d.-a). Getting Started with Pi Camera. projects.raspberrypi.org. https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
* raspberrypi.org. (n.d.-b). Physical Computing with Python. projects.raspberrypi.org. https://projects.raspberrypi.org/en/projects/physical-computing/11
* raspberrypi.org. (n.d.-c). Raspberry pi projects: Parent detector. projects.raspberrypi.org. https://projects.raspberrypi.org/en/projects/parent-detector/1
* RPI cam Web Interface - Raspberry Pi Forums. (n.d.). https://forums.raspberrypi.com/viewtopic.php?f=43&t=63276
* RPI-Cam-Web-Interface - eLinux.org. (n.d.). https://elinux.org/RPi-Cam-Web-Interface
* Run Pi camera from ssh. (n.d.). Raspberry Pi Stack Exchange. https://raspberrypi.stackexchange.com/questions/140040/run-pi-camera-from-ssh
* Santos, S., & Santos, S. (2023, July 13). Raspberry Pi: Motion Detection with Email Notifications (Python) | Random Nerd Tutorials. Random Nerd Tutorials. https://randomnerdtutorials.com/raspberry-pi-motion-email-python/#:~:text=In%20this%20project%2C%20you%E2%80%99ll,ll%20use%20the%20gpiozero%20interface.
* using flask to display image files on my pi - Raspberry Pi Forums. (n.d.). https://forums.raspberrypi.com/viewtopic.php?t=58768
* Vcc and Vss pins. (n.d.). https://www.tutorialspoint.com/vcc-and-vss-pins#:~:text=VCC%20(Voltage%20Common%20Collector)%20is,Supply)%20means%20ground%20or%20zero.
* Wittwer, J. (n.d.). Gantt Chart Template for Excel. Vertex42.com. https://www.vertex42.com/ExcelTemplates/excel-gantt-chart.html
