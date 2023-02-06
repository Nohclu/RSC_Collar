class Entry:
    
    def __init__(self, collarId, timestamp):
        self._collarId = collarId
        self._timeStamp = timestamp


    def __getCollarID(self):
        return self._collarId

    def __getTimeStamp(self):
        return self._timeStamp
