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
        # Create a JSON object for each recorded object
            # Session Stats
            # Session Timings
                # A Button Stats
                    # Button Count / Timestamps
                # B Button Stats
                    #
                # Etc




        
