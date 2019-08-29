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
comboStringList = comboInit.comboList
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
        print("Combo Length = {}".format(len(comboString)))
        print("Curr: {:.3f} sec | Prev: {:.3f} sec | Diff: {:.3f} sec".format(button.pressed_Time, comboPrevTime[currIndex], timeDiff))
        # Current Pressed Time - Previous Pressed Time
        if (timeDiff <= 1.25):
            comboString.append(button.actionType)
            print("Combo Continued!")
            print("Current Combo String: {}".format(comboString))
        elif (timeDiff > 1.25):
            # if a valid combo string was last executed add to list of combo strings
            # then clear string for next combo
            comboString.clear()
            comboPrevTime.clear()
            print("Combo Broken!")
    
    # Check if current comboString Matches
    for combo in comboStringList:
        if(combo.comboString == comboString):
            print("{} Detected".format(combo.name))
            comboString.clear()
    
async def checkButtonInput(start_Time, sessionNumber, sessionDate):
    # Check Button Inputs
    for button in buttonList:
        # Primary Button Press
        if button.gpioPin.is_pressed:
            await asyncio.gather(recordButtonPress(button, start_Time, sessionNumber, sessionDate))
            await asyncio.sleep(0.01)

def clearAllButtonStats():
    for button in buttonList:
        button.clearAllStats()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
