class Entry:
    """Stores SQS Message

    Parameters
    ----------
    event: dict, required
    """

    MAPPINGS = {
        "PET_STATUS":"pet",
        "BATTERY_STATUS":"battery",
        "LOCATION":"location"
        }
    
    def __init__(self, event):
        self._collarId = event["collarId"]
        self._timeStamp = event["timestamp"]
        self._messageType = event["messageType"]
        self._data = event["data"][self.MAPPINGS[self._messageType]]

    def getCollarID(self):
        return self._collarId

    def getTimeStamp(self):
        return self._timeStamp

    def getData(self):
        return self._data

    def getEntry(self):
        return {"collarId":self._collarId,
                "data": {
                    self.MAPPINGS[self._messageType]: self._data
                    },
                "timestamp": self._timeStamp
                }