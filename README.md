# ADAS
Advanced driver-assistance systems (ADAS) are electronic systems that assist drivers in driving and parking functions. Through a safe human-machine interface, ADAS increases car and road safety. ADAS systems use automated technology, such as sensors and cameras, to detect nearby obstacles or driver errors and respond accordingly. This repository contains 2 sections of ADAS, first being the Control System section where LiDAR sensor is used to measure the distance of the obstacle in front of the vehicle and second being the Image Processing section where we use a camera sensor to detect the road’s speed limit enabled by preprocessing of the image and feeding these data set to a Convolutional Neural Networks model. 

REQUIREMENTS:
The basics hardware components required for this project is a LIDAR (TFmini-S), a processor (RaspberryPi-4B), and a camera (PiCamera). 

The adaptive cruise control python folder has the code for implementing cruise control with a processor and a LIDAR (Note: The speed limit value and the three looping condition speed value can be changed according to your own will). The Train python file has the code for implementing traffic sign recognition using a convolutional neural network. 
