# -*- coding: utf-8 -*
import serial 
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

ser = serial.Serial("/dev/ttyS0", 115200)

def getTFminiData():
    global speed
    splimit = 70
    while True:
        counts = ser.in_waiting
        if counts > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()
            if recv[0] == 'Y' and recv[1] == 'Y':
                low = int(recv[2].encode('hex'), 16)
                high = int(recv[3].encode('hex'), 16)
                distance = low + high * 256
                if distance < 80 and speed > 0:
                    speed = speed - 1
                elif distance > 80 and distance < 120:
                    speed = speed
                elif distance > 120 and speed < splimit:
                    speed = speed + 1
                print("Distance:")
                print(distance)
                print("\nSpeed:")
                print(speed)
                return speed
    
if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
        x_vals = []
        y_vals = []
        index = count()
        def animate(i):
            x_vals.append(next(index))
            y_vals.append(getTFminiData())
            plt.plot(x_vals , y_vals)
            plt.xlabel('Time')
            plt.ylabel('Speed')
            plt.title('Cruise Control')
        ani = FuncAnimation(plt.gcf(), animate, interval=50)
        plt.show()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close() 


