class Entry:
    """Stores SQS Message

    Parameters
    ----------
    event: dict, required
    """

    mappings = {
        "PET_STATUS":"pet",
        "BATTERY_STATUS":"battery",
        "LOCATION":"location"
        }
    
    def __init__(self, event):
        self._collarId = event["collarId"]
        self._timeStamp = event["timestamp"]
        self._messageType = event["messageType"]
        self._data = event["data"][self.mappings[self._messageType]]

    def getCollarID(self):
        return self._collarId

    def getTimeStamp(self):
        return self._timeStamp

    def getData(self):
        return self._data

    def getMessageType(self):
        return self._messageType

    def getEntry(self):
        return {"collarId":self._collarId,
                "data": {
                    self.mappings[self._messageType]: self._data
                    },
                "messageType": self._messageType,
                "timestamp": self._timeStamp
                }