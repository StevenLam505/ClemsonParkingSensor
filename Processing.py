from DailyTrendsDictionary import *
from datetime import datetime
import requests
import os
import psycopg2

occupancyURL = "https://2zi3sm5r6e.execute-api.us-east-1.amazonaws.com/api/occupancy"
occupancyResponse = requests.get(url = occupancyURL)
occupancyData = occupancyResponse.json()

lotInfoURL = "https://2zi3sm5r6e.execute-api.us-east-1.amazonaws.com/api/lotinfo"
lotInfoResponse = requests.get(url = lotInfoURL)
lotInfoData = lotInfoResponse.json()

# Calculates the current capacity and returns as a %
def CalculateCurrentCapacity(parkingOccupancy, lotInfo): 
    filledSpots = 0
    totalSpots = 1
    for parkingSpace in parkingOccupancy:
        lotId = parkingSpace['lotname']
        if(parkingSpace['occupancy']) == True:
            filledSpots += 1

    for lot in lotInfo:
        if(lot['lotname'] == lotId):
            totalSpots = lot['totalspaces']

    return round(filledSpots/totalSpots * 100, 2)

# Calculates the current occupancy every 15 minutes
def UpdateTrends(parkingOccupancy, lotInfo):
    currentDate = datetime.now().date()
    currentTime = datetime.now().time().strftime('%H:%M:%S')
    currentOccupancy = CalculateCurrentCapacity(parkingOccupancy, lotInfo)
    conn = psycopg2.connect("postgresql://getonly:Ew7uOPF4K1SxARyA0moRJA@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

    with conn.cursor() as cur:
        insertCommand = '''INSERT INTO public.dailyoccupancytrends (date, time, lotname, occupancypct) 
        VALUES ('{}','{}','{}',{})'''.format(currentDate, currentTime, 'C-11', currentOccupancy)
        cur.execute(insertCommand)
        conn.commit()


UpdateTrends(occupancyData, lotInfoData)
