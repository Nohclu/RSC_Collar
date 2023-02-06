from entry import Entry

class Battery(Entry):
    
    def __init__(self, collarId, timestamp, percentage):
        super().__init__(collarId,timestamp)
        self._percentage = percentage

    def getCollarID(self):
        return self.__getCollarID()

    def getTimeStamp(self):
        return self.__getTimeStamp()

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self.getCollarID(),
                "data": {
                    "percentage": self._percentage
                },
                "timestamp": self.getTimeStamp()
                }