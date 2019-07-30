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
            clearAllButtonStats()
            start_Time = time.time()
            print("Button Stats Cleared / Time Reset - Session Recorded")
            recordingSession.start()
        
        checkButtonInput(start_Time)
            
        sleep(0.01)

def recordButtonPress(button, start_Time):
    button.incrementButtonCount()
    button.calcCurrentButtonTimings(start_Time)
    button.showStats()
    button.logActionToTxtFile()

def checkButtonInput(start_Time):
    # Button Inputs
    if cInit.button_A.gpioPin.is_pressed:
        recordButtonPress(cInit.button_A, start_Time)
    
    if cInit.button_B.gpioPin.is_pressed:
        recordButtonPress(cInit.button_B, start_Time)
    
    if cInit.button_X.gpioPin.is_pressed:
        recordButtonPress(cInit.button_X, start_Time)
    
    if cInit.button_Y.gpioPin.is_pressed:
        recordButtonPress(cInit.button_Y, start_Time)
    
    if cInit.button_LB.gpioPin.is_pressed:
        recordButtonPress(cInit.button_LB, start_Time)
    
    if cInit.button_RB.gpioPin.is_pressed:
        recordButtonPress(cInit.button_RB, start_Time)
    
    if cInit.button_LT.gpioPin.is_pressed:
        recordButtonPress(cInit.button_LT, start_Time)            
    
    if cInit.button_RT.gpioPin.is_pressed:
        recordButtonPress(cInit.button_RT, start_Time)
    
    if cInit.button_Up.gpioPin.is_pressed:
        recordButtonPress(cInit.button_Up, start_Time)
    
    if cInit.button_Down.gpioPin.is_pressed:
        recordButtonPress(cInit.button_Down, start_Time)
    
    if cInit.button_Left.gpioPin.is_pressed:
        recordButtonPress(cInit.button_Left, start_Time)            
    
    if cInit.button_Right.gpioPin.is_pressed:
        recordButtonPress(cInit.button_Right, start_Time)

def clearAllButtonStats():
    cInit.button_A.clearAllStats()
    cInit.button_B.clearAllStats()
    cInit.button_X.clearAllStats()
    cInit.button_Y.clearAllStats()
    cInit.button_LB.clearAllStats()
    cInit.button_RB.clearAllStats()
    cInit.button_LT.clearAllStats()
    cInit.button_RT.clearAllStats()
    cInit.button_Up.clearAllStats()
    cInit.button_Down.clearAllStats()
    cInit.button_Right.clearAllStats()
    cInit.button_Left.clearAllStats()
    
if __name__ == '__main__':
    main()