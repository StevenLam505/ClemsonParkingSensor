from datetime import datetime
import time
import serial
import psycopg2
import random
import threading
from threading import Thread, Lock

lock = Lock()
spot_list = list()
for i in range(0,20):
    spot_list.append(False)
conn = psycopg2.connect("postgresql://getonly:Ew7uOPF4K1SxARyA0moRJA@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

def thread_func(num1, num2, name):
    # function to get input from 1 sensor
    arduino = serial.Serial('COM{}'.format(str(num1)), 9600)
    occupied = False
    int_var  = 0
    my_list = [0,0,0,0,0,0,0,0,0,0]

    while True:
        now = datetime.now()
        hour = now.strftime("%H")
        time.sleep(1)

        arduino.write(str.encode(hour)) # sending hour info
        byte_var = arduino.read(1) # get occupancy data

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
            print("Spot {} is OCCUPIED".format(name))
        else:
            occupied = False
            print("Spot {} is AVAILABLE".format(name))
        spot_list[num2] = occupied

        time.sleep(0) # yield to another thread
        print(str(my_list))

if __name__=="__main__":
    t1 = threading.Thread(target=thread_func, args=(5, 0, "A0"))
    t2 = threading.Thread(target=thread_func, args=(3, 1, "A1"))

    t1.start()
    t2.start()

    while True:
        for i in range(2,20):
            spot_list[i] = bool(random.getrandbits(1))
        lock.acquire()
        dummy_list = spot_list.copy()
        lock.release()
        for i in range(0,20):
            spot_name = "A" + str(i)
            with conn.cursor() as cur:
                if(dummy_list[i] == False):
                    cur.execute('''UPDATE public.parkingoccupancy
                        SET occupancy = FALSE
                        WHERE spotname = '{}'
                        '''.format(spot_name))
                else:
                    cur.execute('''UPDATE public.parkingoccupancy
                        SET occupancy = TRUE
                        WHERE spotname = '{}'
                        '''.format(spot_name))
                conn.commit()    
        time.sleep(0)