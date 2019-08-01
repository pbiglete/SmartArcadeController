import cInit
from time import sleep
import time
import datetime
from recorderSession import session

def main():
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
        
        checkButtonInput(buttonList, start_Time)
            
        sleep(0.01)

def recordButtonPress(button, start_Time):
    button.incrementButtonCount()
    button.calcCurrentButtonTimings(start_Time)
    button.showStats()
    button.logActionToTxtFile()

def checkButtonInput(buttonList, start_Time):
    # Check Button Inputs
    for button in buttonList:
        if button.gpioPin.is_pressed:
            recordButtonPress(button, start_Time)

def clearAllButtonStats(buttonList):
    for button in buttonList:
        button.clearAllStats()
    
if __name__ == '__main__':
    main()