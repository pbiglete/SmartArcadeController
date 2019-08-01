import time
from gpiozero import Button

class controllerButton:   
    name = ""
    buttonCount = 0
    actionType = ""
    gpioPin = None
    pressed_Time = 0
    released_Time = 0
    hold_Time = 0
    sum_HoldTime = 0
    avg_HoldTime = 0
    pressed_Timestamps = []
    
    def __init__(self, buttonName = "", actionType = "None", buttonCount = 0, gpioPIN = None):
        self.name = buttonName
        self.actionType = actionType
        self.buttonCount = buttonCount
        self.gpioPin = gpioPIN

    def setName(self, buttonName):
        self.name = buttonName

    def setActionType(self, actionType):
        self.actionType = actionType

    def incrementButtonCount(self):
        self.buttonCount += 1
        
    def clearButtonCount(self):
        self.buttonCount = 0
        
    def calcCurrentButtonTimings(self, start_Time):
        self.pressed_Time = time.time() - start_Time
        self.pressed_Timestamps.append(self.pressed_Time)
        self.gpioPin.wait_for_release()
        self.released_Time = time.time() - start_Time
        self.hold_Time = self.released_Time - self.pressed_Time
        self.sum_HoldTime = self.sum_HoldTime + self.hold_Time
        self.avg_HoldTime = self.sum_HoldTime / self.buttonCount
    
    def clearCurrentButtonTimings(self):
        self.pressed_Time = 0
        self.released_Time = 0
        self.hold_Time = 0
        
    def clearAvgButtonTimings(self):
        self.avg_HoldTime = 0
        self.sum_HoldTime = 0

    def showStats(self):   
        print(self.name + " (" + self.actionType + "): " + str(self.buttonCount) +
              " | Time Pressed: " + str("{:.3f} sec".format(self.pressed_Time)) +
              " | Held for: " + str("{:.3f} sec".format(self.hold_Time)) +
              " | Avg. Hold Time: " + str("{:.3f} sec".format(self.avg_HoldTime)))
        
    def clearAllStats(self):
        self.clearCurrentButtonTimings()
        self.clearAvgButtonTimings()
        self.clearButtonCount()
        self.pressed_Timestamps.clear()

    def logActionToTxtFile(self):
        buttonLogFile = open("Action_Log.txt", "a")
        buttonLogFile.write("Time: " + str("{:.3f} sec".format(self.pressed_Time)) +
                            " | " + self.name + ": " + str(self.buttonCount) + "\n")
        buttonLogFile.close()
        
        
    
        
