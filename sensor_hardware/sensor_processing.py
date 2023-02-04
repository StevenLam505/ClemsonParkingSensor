from datetime import datetime
import time
import serial
#import os
import psycopg2
import random
import threading

arduino_uno = serial.Serial('COM5', 9600)
arduino_mega = serial.Serial('COM3', 9600)
occupied = False
occupied2 = False
int_var = 0
int_var2 = 0
my_list = [0,0,0,0,0]
my_list2 = [0,0,0,0,0]
spot_list = list()
for i in range(0,20):
    spot_list.append(False)
#print(str(spot_list))
conn = psycopg2.connect("postgresql://getonly:Ew7uOPF4K1SxARyA0moRJA@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

while True:
    now = datetime.now()
    hour = now.strftime("%H")
    # print("The current time is", now);
    time.sleep(1)

    arduino_uno.write(str.encode(hour)) #sending hour info to arduino
    arduino_mega.write(str.encode(hour))
    byte_var = arduino_uno.read(1) #reading occupied info from arduino
    byte_var2 = arduino_mega.read(1)
    print(str(byte_var)+str(byte_var2))

    if byte_var == b'1':
        int_var = 1
    else:
        int_var = 0

    if byte_var2 == b'1':
        int_var2 = 1
    else:
        int_var2 = 0
    # getting an average to decide if spot is available
    my_list.append(int_var)
    my_list.pop(0)
    average = round(sum(my_list)/len(my_list),0)
    my_list2.append(int_var2)
    my_list2.pop(0)
    average2 = round(sum(my_list2)/len(my_list2),0)

    if average == 1.0:
        occupied = True
        print("The spot is OCCUPIED", average)
    else:
        occupied = False
        print("The spot is AVAILABLE", average)
    spot_list[0] = occupied

    if average2 == 1.0:
        occupied2 = True
        print("The spot2 is OCCUPIED", average2)
    else:
        occupied2 = False
        print("The spot2 is AVAILABLE", average2)
    spot_list[1] = occupied2

    for i in range(2,20):
        spot_list[i] = bool(random.getrandbits(1))

    
    for i in range(0,20):
        spot_name = "A" + str(i)
        with conn.cursor() as cur:
            if(spot_list[i] == False):
                cur.execute('''UPDATE public.parkingoccupancy
                        SET occupancy = FALSE
                        WHERE spotname = '{}'
                        '''.format(spot_name))
            else:
                cur.execute('''UPDATE public.parkingoccupancy
                    SET occupancy = TRUE
                    WHERE spotname = '{}'
                    '''.format(spot_name))
            #res = cur.fetchall()
            conn.commit()
            #print(cur)
    print(str(my_list))
    print(str(my_list2))



