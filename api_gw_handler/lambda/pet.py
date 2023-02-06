from entry import Entry

class Pet(Entry):
    
    def __init__(self, collarId, timestamp, status, heartrate):
        super().__init__(collarId, timestamp)
        self._status = status
        self._heartrate = heartrate

    def getCollarID(self):
        return self.__getCollarID()

    def getTimeStamp(self):
        return self.__getTimeStamp()

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self.getCollarID(),
                "data": {
                    "status": self._status,
                    "heartrate": self._heartrate
                },
                "timestamp": self.getTimeStamp()
                }