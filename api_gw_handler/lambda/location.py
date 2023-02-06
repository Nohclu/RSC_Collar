class Location:
    
    def __init__(self, collarId, timestamp, lat, long):
        self._collarId = collarId
        self._timeStamp = timestamp
        self._lat = lat
        self._long = long

    def getCollarID(self):
        return self._collarId

    def getTimeStamp(self):
        return self._timeStamp

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self._collarId,
                "data": {
                    "lat": self._lat,
                    "long": self._long
                },
                "timestamp": self._timeStamp
                }