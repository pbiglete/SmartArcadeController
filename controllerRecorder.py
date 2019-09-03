import cInit
from time import sleep
import time
import os
import datetime
import asyncio
import json
import comboInit
from recorderSession import session

buttonList = cInit.buttonList
comboQueue = []
comboString = []
comboPrevTime = []
comboStringDict = comboInit.comboDict
sessionList = []

async def main():
    sessionNumber = 0
    start_Time = time.time()
    recordingSession = session(sessionNumber, datetime.datetime.now().date(), datetime.datetime.now().time())

    print("Controller Recorder Active")
    print("--------------------------")

    while True:

        # Reset & Record Session
        if cInit.button_Select.gpioPin.is_held:
            print("Release to Clear Button Stats and Reset Time")        
            cInit.button_Select.gpioPin.wait_for_release()
            recordingSession.end(buttonList)
            sessionList.append(recordingSession.data)
            
            with open('sessions.json', 'w') as JSON_file:
                json.dump(sessionList, JSON_file, indent=4)
                
            sessionNumber += 1
            recordingSession = session(sessionNumber, datetime.datetime.now().date(), datetime.datetime.now().time())
            clearAllButtonStats()
            start_Time = time.time()
            print("Button Stats Cleared / Time Reset - Session Recorded")
            recordingSession.start()
        
        await asyncio.gather(checkButtonInput(start_Time, recordingSession.sessionNumber, recordingSession.date))
        await asyncio.sleep(0.01)

async def recordButtonPress(button, start_Time, sessionNumber, sessionDate):
    button.incrementButtonCount()
    button.calcCurrentButtonTimings(start_Time)
    button.showStats()
    button.logActionToTxtFile(sessionNumber, sessionDate)

    # Button Combo String Detection      
    if len(comboString) == 0: #combo string is empty, start combo
        comboPrevTime.append(button.pressed_Time) # Save Current Time
        comboString.append(button.actionType) # Add to Combo Chain/String
        print("Combo Started! - {}".format(comboString))
    elif len(comboString) > 0: #combo string is ongoing
        currIndex = len(comboPrevTime) - 1
        timeDiff = button.pressed_Time - comboPrevTime[currIndex]
        print("Combo Length = {} | Curr: {:.3f} sec | Prev: {:.3f} sec | Diff: {:.3f} sec".format(len(comboString), button.pressed_Time, comboPrevTime[currIndex], timeDiff))
        # Current Pressed Time - Previous Pressed Time
        if (timeDiff <= 1.275) and (button.isDirectional == False):
            comboString.append(button.actionType)
            print("Combo Continued! -> Current Combo String: {}".format(comboString))
            
            # Check if current comboString Matches
            if len(comboString) > 1:       
                comboStr = ' '.join(map(str, comboString))
                # print(comboStr)
                if(comboStr in comboStringDict):
                    print("{} Excuted! -> Combo String Reset!".format(comboStringDict[comboStr].name))
                    comboString.clear()
                    comboPrevTime.clear()
        elif (timeDiff > 1.275) and (button.isDirectional == False):
            # then clear string for next combo
            comboString.clear()
            comboPrevTime.clear()
            print("Combo Broken -> Combo String Reset!")
        elif (timeDiff <= 0.250) and (button.isDirectional == True):
            comboString.append(button.actionType)
            print("Combo Continued! -> Current Combo String: {}".format(comboString))       
            # Check if current comboString Matches
            if len(comboString) > 1:       
                comboStr = ' '.join(map(str, comboString))
                # print(comboStr)
                if(comboStr in comboStringDict):
                    print("{} Excuted! -> Combo String Reset!".format(comboStringDict[comboStr].name))
                    comboString.clear()
                    comboPrevTime.clear()
        elif (timeDiff > 0.250) and (button.isDirectional == True):
            # then clear string for next combo
            comboString.clear()
            comboPrevTime.clear()
            print("Combo Broken -> Combo String Reset!")        
                
async def checkButtonInput(start_Time, sessionNumber, sessionDate):
    # Check Button Inputs
    for button in buttonList:
        # Primary Button Press
        if button.gpioPin.is_pressed:
            await recordButtonPress(button, start_Time, sessionNumber, sessionDate)

def clearAllButtonStats():
    for button in buttonList:
        button.clearAllStats()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
