class Battery:
    
    def __init__(self, collarId, timestamp, percentage):
        self._collarId = collarId
        self._timeStamp = timestamp
        self._percentage = percentage

    def getCollarID(self):
        return self._collarId

    def getTimeStamp(self):
        return self._timeStamp

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self._collarId,
                "data": {
                    "percentage": self._percentage
                },
                "timestamp": self._timeStamp
                }