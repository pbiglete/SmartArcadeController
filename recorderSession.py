import datetime

class session:
    # Session Number
    # Date
    # Start Time
    # End Time
    # Total Button Presses
    # Button Presses per Minute

    def __init__(self, sessionNumber, date, startTime):
        self.sessionNumber = sessionNumber
        self.date = date
        self.startTime = startTime

    def start(self):
        self.date = datetime.datetime.now().date()
        self.startTime = datetime.datetime.now().time()
        print("Session Started - {} : {}".format(self.date, self.startTime))

    def end(self, totalButtonPresses, buttonsPerMinute):
        self.endTime = datetime.datetime.now().time()
        print("Session Ended - {}".format(self.endTime))

        
