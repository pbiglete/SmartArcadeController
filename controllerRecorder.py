import cInit
from time import sleep
import time

start_Time = time.time()

print("Controller Recorder Active")
print("--------------------------")

while True:
    
    # Reset
    if cInit.button_Select.gpioPin.is_held:
        print("Release to Clear Button Stats and Reset Time")
        cInit.button_Select.wait_for_release()
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
        print("Button Stats Cleared / Time Reset")
    
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
