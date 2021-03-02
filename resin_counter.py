import os
import datetime
import time
import math

counter = 0

def verifyResin(resinCount):
    return 0 <= resinCount <= 160

def refreshScreen(timeToMax, currentResin):
    os.system("cls")
    print("================RESIN COUNTER================\n\n")
    print("Estimated current amount of resin: {}".format(currentResin))
    print("Estimated time left to full resin: {}:{}:{}".format(timeToMax.hour,timeToMax.minute,timeToMax.second))

def updateTimeResin(currentTime, currentResin):
    global counter
    if(currentTime.hour >= 0):
        if(currentTime.minute >= 0):
            if(currentTime.second > 0):
                currentTime = datetime.time(currentTime.hour, currentTime.minute, currentTime.second - 1)
            else:
                currentTime = datetime.time(currentTime.hour, currentTime.minute-1, 59)
                if(counter < 8):
                    counter += 1
                else:
                    counter = 0
                    currentResin += 1
        else:
            currentTime = datetime.time(currentTime.hour - 1, 59, 59)
    else:
        currentTime = datetime.time(0,0,0)
    return [currentTime, currentResin]


def main():
    currentResin = ""
    while(not isinstance(currentResin, int)):
        os.system("cls")
        print("================RESIN COUNTER================\n\n")
        try:
            currentResin = int(input("Enter current amount of resin: "))
            while(not verifyResin(currentResin)):
                os.system("cls")
                print("================RESIN COUNTER================\n\n")
                try:
                    print("I didn't think you were braindead enough to put a number like that.")
                    currentResin = int(input("Enter current amount of resin: "))
                except ValueError:
                    print("Put a number, fool.")
                    time.sleep(1)
            rawTime = float((160-currentResin) * 8)
            hoursLeft = float(rawTime / 60)
            minsLeft = math.ceil((float(hoursLeft) - int(hoursLeft)) * 60)
            secsLeft = math.ceil((float(minsLeft) - int(minsLeft)) * 60)
            timeToMax = datetime.time(int(hoursLeft),int(minsLeft),int(secsLeft))
            while(True):
                refreshScreen(timeToMax, currentResin)
                time.sleep(1)
                currentResinTime = updateTimeResin(timeToMax, currentResin)
                timeToMax = currentResinTime[0]
                currentResin = currentResinTime[1]
                if(timeToMax.hour == 0 and timeToMax.minute == 0 and timeToMax.second == 0):
                    refreshScreen(timeToMax, currentResin)
                    print("IT'S GAMER TIME BABY GO GET THAT TRASH")
                    break
        except ValueError:
            print("Put a number, fool.")
            time.sleep(1)

main()
