class Pet:
    
    def __init__(self, collarId, timestamp, status, heartrate):
        self._collarId = collarId
        self._timeStamp = timestamp
        self._status = status
        self._heartrate = heartrate

    def getCollarID(self):
        return self._collarId

    def getTimeStamp(self):
        return self._timeStamp

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self._collarId,
                "data": {
                    "status": self._status,
                    "heartrate": self._heartrate
                },
                "timestamp": self._timeStamp
                }