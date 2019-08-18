import cInit
from time import sleep
import time
import datetime
import asyncio
from recorderSession import session

async def main():
    buttonList = cInit.buttonList
    sessionList = []

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
            sessionList.append(recordingSession)
            sessionNumber += 1
            recordingSession = session(sessionNumber, datetime.datetime.now().date(), datetime.datetime.now().time())
            clearAllButtonStats(buttonList)
            start_Time = time.time()
            print("Button Stats Cleared / Time Reset - Session Recorded")
            recordingSession.start()
        
        await asyncio.gather(checkButtonInput(buttonList, start_Time, recordingSession.sessionNumber, recordingSession.date))
        await asyncio.sleep(0.01)

async def recordButtonPress(button, start_Time, sessionNumber, sessionDate):
    button.incrementButtonCount()
    button.calcCurrentButtonTimings(start_Time)
    button.showStats()
    button.logActionToTxtFile(sessionNumber, sessionDate)

async def checkButtonInput(buttonList, start_Time, sessionNumber, sessionDate):
    # Check Button Inputs
    for button in buttonList:
        # Primary Button Press
        if button.gpioPin.is_pressed:
            await recordButtonPress(button, start_Time, sessionNumber, sessionDate)

def clearAllButtonStats(buttonList):
    for button in buttonList:
        button.clearAllStats()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
