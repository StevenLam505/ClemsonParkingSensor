import random
from datetime import datetime, timedelta

currentDate = datetime.now().date()

#for x in range(53):
 #       print(str(random.randint(0,100)) + ",", end=" ")
    

for x in range(53):
    test = (datetime.now().replace(hour=7,minute=0,second=0,microsecond=0) + (timedelta(minutes=15) * x)).strftime('%H:%M:%S')
    print('''INSERT INTO public.dailyoccupancytrends (date, time, lotname, occupancypct) 
        VALUES ('{}','{}','{}',{})'''.format(currentDate, test, 'C-11', 0))