

class combo:
    def __init__(self, name = "", comboString = [], comboType = None, comboCount = 0):
        self.name = name
        self.comboString = comboString
        self.comboType = comboType
        self.comboCount = comboCount
    
    def incrementComboCount(self):
        self.comboCount += 1
    def clearComboCount(self):
        self.comboCount = 0