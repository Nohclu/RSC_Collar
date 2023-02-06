from entry import Entry

class Location(Entry):
    
    def __init__(self, collarId, timestamp, lat, long):
        super().__init__(collarId, timestamp)
        self._lat = lat
        self._long = long

    def getCollarID(self):
        return self.__getCollarID()

    def getTimeStamp(self):
        return self.__getTimeStamp()

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self.getCollarID(),
                "data": {
                    "lat": self._lat,
                    "long": self._long
                },
                "timestamp": self.getTimeStamp()
                }