
class Job:

    def __init__(self,time:int):
        self._timeForJob = time
    
    def SetTime(self,newTime:int):
        self._timeForJob = newTime
    
    def GetTime(self) -> int:
        return self._timeForJob
    
    def __lt__(self,other):
        if self.GetTime() < other.GetTime():
            return True
        else:
            return False