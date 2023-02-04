from datetime import datetime
import time
import serial

arduino = serial.Serial('COM5', 9600)
occupied = False
int_var = 0
my_list = [0,0,0,0,0]

while True:
    now = datetime.now()
    hour = now.strftime("%H")
    # print("The current time is", now);
    time.sleep(1)

    arduino.write(str.encode(hour)) #sending hour info to arduino
    byte_var = arduino.read(1) #reading occupied info from arduino

    if byte_var == b'1':
        int_var = 1
    else:
        int_var = 0
    # getting an average to decide if spot is available
    my_list.append(int_var)
    my_list.pop(0)
    average = round(sum(my_list)/len(my_list),0)

    if average == 1.0:
        occupied = True
        print("The spot is OCCUPIED", average)
    else:
        occupied = False
        print("The spot is AVAILABLE", average)


