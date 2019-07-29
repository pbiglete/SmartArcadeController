import cInit
from time import sleep
import time
import datetime
from recorderSession import session

List = []

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
        totalButtonPresses = cInit.button_A.buttonCount + cInit.button_B.buttonCount + cInit.button_X.buttonCount + cInit.button_Y.buttonCount + cInit.button_LB.buttonCount + cInit.button_RB.buttonCount + cInit.button_LT.buttonCount + cInit.button_RT.buttonCount + cInit.button_Up.buttonCount + cInit.button_Down.buttonCount + cInit.button_Left.buttonCount + cInit.button_Right.buttonCount
        recordingSession.end(totalButtonPresses, 0)
        List.append(recordingSession)
        sessionNumber += 1
        recordingSession = session(sessionNumber, datetime.datetime.now().date(), datetime.datetime.now().time())
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
        start_Time = time.time()
        print("Button Stats Cleared / Time Reset - Session Recorded")
        recordingSession.start()
    
    if cInit.button_A.gpioPin.is_pressed:
        cInit.button_A.incrementButtonCount()
        cInit.button_A.calcCurrentButtonTimings(start_Time)
        cInit.button_A.showStats()
        cInit.button_A.logActionToTxtFile()
        
    if cInit.button_B.gpioPin.is_pressed:
        cInit.button_B.incrementButtonCount()
        cInit.button_B.calcCurrentButtonTimings(start_Time)
        cInit.button_B.showStats()
        cInit.button_B.logActionToTxtFile()
        
    if cInit.button_X.gpioPin.is_pressed:
        cInit.button_X.incrementButtonCount()
        cInit.button_X.calcCurrentButtonTimings(start_Time)
        cInit.button_X.showStats()
        cInit.button_X.logActionToTxtFile()
        
    if cInit.button_Y.gpioPin.is_pressed:
        cInit.button_Y.incrementButtonCount()
        cInit.button_Y.calcCurrentButtonTimings(start_Time)
        cInit.button_Y.showStats()
        cInit.button_Y.logActionToTxtFile()
        
           
    sleep(0.01)
