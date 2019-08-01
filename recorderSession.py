import datetime

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

    def start(self):
        self.date = datetime.datetime.now().date()
        self.startTime = datetime.datetime.now().time()
        print("Session {} Started - {} : {}".format(self.sessionNumber, self.date, self.startTime))

    def end(self, buttonList = [], *args):
        self.endTime = datetime.datetime.now().time()
        print("Session {} Ended - {}".format(self.sessionNumber, self.endTime))
        self.buttonList = buttonList
        self.convertStatsToTxt(buttonList)
        # Create a JSON object for each recorded object
            # Session Stats
            # Session Timings
                # A Button Stats
                    # Button Count / Timestamps
                # B Button Stats
                    #
                # Etc

    def convertStatsToTxt(self, buttonList = [], *args):
        totalButtonCount = 0
        
        for button in buttonList:
            totalButtonCount += button.buttonCount
            
        if totalButtonCount is 0:
            print("EMPTY SESSION - NO FILE CREATED")
            pass
        else:
            sessionFile = open("session_{}_{}.txt".format(self.sessionNumber, self.date.strftime("%b-%d-%Y")), "a")
            sessionFile.write("Session {} Stats - {} @ {} - {}\n".format(self.sessionNumber, self.date.strftime("%b %d, %Y"), self.startTime.strftime("%H:%M:%S"), self.endTime.strftime("%H:%M:%S")))
            for button in buttonList:
                sessionFile.write("{} | {} | Usage Rate: {}/{} ({:.2f}%) | Avg. Hold Time: {:.3f} sec \n".format(button.name, button.actionType, button.buttonCount, totalButtonCount, ((button.buttonCount / totalButtonCount) * 100), button.avg_HoldTime))
                sessionButtonFile = open("session_{}_{}_{}_timings.txt".format(self.sessionNumber, self.date.strftime("%b-%d-%Y"), button.name.replace(" ", "_")), "a")
                
                for timestamp in button.pressed_Timestamps:
                    sessionButtonFile.write("{:.3f} sec\n".format(timestamp))
            
        sessionFile.close()
        sessionButtonFile.close()

