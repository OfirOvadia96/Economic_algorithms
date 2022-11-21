from Job import Job

class Student:

    def __init__(self):
        self._sumOfTimeForJobs = 0
        self._listOfJobs = []
    
    
    def AddToWorkingTime(self,NewJob:Job):
        self._sumOfTimeForJobs = self._sumOfTimeForJobs + NewJob.GetTime()
        self._listOfJobs.append(NewJob.GetTime())
        

    def RemoveJobByIndex(self,index:int):
        self._listOfJobs.remove(index)
    
    def GetTimeJobs(self):
        return self._sumOfTimeForJobs



    

