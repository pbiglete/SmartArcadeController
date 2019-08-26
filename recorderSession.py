import datetime
import os
# import matplotlib.pyplot as plt
import json

class session:
    # Session Number
    # Date
    # Start Time
    # End Time
    # Button Statistics

    def __init__(self, sessionNumber, date, startTime):
        self.sessionNumber = sessionNumber
        self.date = date
        self.startTime = startTime
        self.buttonList = []
        self.data = ""

    def start(self):
        self.date = datetime.datetime.now().date()
        self.startTime = datetime.datetime.now().time()
        print("Session {} Started - {} : {}".format(self.sessionNumber, self.date.strftime("%b %d, %Y"), self.startTime.strftime("%H:%M:%S")))

    def end(self, buttonList = [], *args):
        self.endTime = datetime.datetime.now().time()
        print("Session {} Ended - {}".format(self.sessionNumber, self.endTime.strftime("%H:%M:%S")))
        self.buttonList = buttonList
        self.convertStatsToTxt(buttonList)
        self.data = self.convertSessionToJSONString(buttonList)
        # self.graphStats()

#    def graphStats(self):
#        buttonCounts = []
#        buttonLabels = []
#        buttonColors = ['limegreen', 'tomato', 'deepskyblue', 'gold',
#                        'orange', 'darkorange', 'plum', 'darkviolet',
#                        'lightsteelblue', 'lightslategray', 'steelblue', 'darkturquoise']
#        
#        for button in self.buttonList:
#            buttonLabels.append(button.name)
#            buttonCounts.append(button.buttonCount)
#            
#        plt.pie(buttonCounts, labels=buttonLabels, colors=buttonColors, autopct='%1.1f%%', startangle=130)
#        plt.axis('equal')
#        plt.show()

    def convertSessionToJSONString(self, buttonList = [], * args):   
        # Create a JSON object for each recorded object
        # Session Stats
        # Session Timings
            # A Button Stats
                # Button Count / Timestamps
            # B Button Stats
                #
            # Etc
            
        totalButtonCount = 0
        
        for button in buttonList:
            totalButtonCount += button.buttonCount
        
        temp = {
            "sessionNumber": self.sessionNumber,
            "date": self.date.strftime("%b %d, %Y"),
            "startTime": self.startTime.strftime("%H:%M:%S"),
            "endTime": self.endTime.strftime("%H:%M:%S"),
            "totalButtonCount": totalButtonCount,
            "buttonList": [
                {"name": buttonList[0].name,
                     "type": buttonList[0].actionType,
                     "usagePercent": (buttonList[0].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[0].buttonCount,
                     "timestamps": buttonList[0].pressed_Timestamps},
                {"name": buttonList[1].name,
                     "type": buttonList[1].actionType,
                     "usagePercent": (buttonList[1].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[1].buttonCount,
                     "timestamps": buttonList[1].pressed_Timestamps},
                {"name": buttonList[2].name,
                     "type": buttonList[2].actionType,
                     "usagePercent": (buttonList[2].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[2].buttonCount,
                     "timestamps": buttonList[2].pressed_Timestamps},
                {"name": buttonList[3].name,
                     "type": buttonList[3].actionType,
                     "usagePercent": (buttonList[3].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[3].buttonCount,
                     "timestamps": buttonList[3].pressed_Timestamps},
                {"name": buttonList[4].name,
                     "type": buttonList[4].actionType,
                     "usagePercent": (buttonList[4].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[4].buttonCount,
                     "timestamps": buttonList[4].pressed_Timestamps},
                {"name": buttonList[5].name,
                     "type": buttonList[5].actionType,
                     "usagePercent": (buttonList[5].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[5].buttonCount,
                     "timestamps": buttonList[5].pressed_Timestamps},
                {"name": buttonList[6].name,
                     "type": buttonList[6].actionType,
                     "usagePercent": (buttonList[6].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[6].buttonCount,
                     "timestamps": buttonList[6].pressed_Timestamps},
                {"name": buttonList[7].name,
                     "type": buttonList[7].actionType,
                     "usagePercent": (buttonList[7].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[7].buttonCount,
                     "timestamps": buttonList[7].pressed_Timestamps},
                {"name": buttonList[8].name,
                     "type": buttonList[8].actionType,
                     "usagePercent": (buttonList[8].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[8].buttonCount,
                     "timestamps": buttonList[8].pressed_Timestamps},
                {"name": buttonList[9].name,
                     "type": buttonList[9].actionType,
                     "usagePercent": (buttonList[9].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[9].buttonCount,
                     "timestamps": buttonList[9].pressed_Timestamps},
                {"name": buttonList[10].name,
                     "type": buttonList[10].actionType,
                     "usagePercent": (buttonList[10].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[10].buttonCount,
                     "timestamps": buttonList[10].pressed_Timestamps},
                {"name": buttonList[11].name,
                     "type": buttonList[11].actionType,
                     "usagePercent": (buttonList[11].buttonCount / totalButtonCount) * 100,
                     "bCount": buttonList[11].buttonCount,
                     "timestamps": buttonList[11].pressed_Timestamps}, 
            ]
        }

        return temp

    def convertStatsToTxt(self, buttonList = [], *args):
        totalButtonCount = 0
        
        for button in buttonList:
            totalButtonCount += button.buttonCount
            
        if totalButtonCount is 0:
            print("EMPTY SESSION - NO FILE CREATED")
            pass
        else:
            sessionFileName = "session_{}_{}.txt".format(self.sessionNumber, self.date.strftime("%b-%d-%Y"))
            sessionPath = "session_{}_{}".format(self.sessionNumber, self.date.strftime("%b-%d-%Y"))
            sessionFilePath = os.path.join(sessionPath, sessionFileName)
            
            if not os.path.exists(sessionPath):
                os.makedirs(sessionPath)

            sessionFile = open(sessionFilePath, "a")
            sessionFile.write("Session {} Stats - {} @ {} - {}\n".format(self.sessionNumber, self.date.strftime("%b %d, %Y"), self.startTime.strftime("%H:%M:%S"), self.endTime.strftime("%H:%M:%S")))
            
            for button in buttonList:
                
                sessionFile.write("{} | {} | Usage Rate: {}/{} ({:.2f}%) | Avg. Hold Time: {:.3f} sec \n".format(button.name, button.actionType, button.buttonCount, totalButtonCount, ((button.buttonCount / totalButtonCount) * 100), button.avg_HoldTime))
                
                sessionButtonFileName = "session_{}_{}_{}_timings.txt".format(self.sessionNumber, self.date.strftime("%b-%d-%Y"), button.name.replace(" ", "_"))
                sessionButtonFilePath = os.path.join(sessionPath, sessionButtonFileName)
                sessionButtonFile = open(sessionButtonFilePath, "a")
                
                for timestamp in button.pressed_Timestamps:
                    sessionButtonFile.write("{:.3f} sec\n".format(timestamp))
            
        sessionFile.close()
        sessionButtonFile.close()

        