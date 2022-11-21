from Job import Job

class Jobs:

    def __init__(self):
        self._jobsArray = []
        self._sumOfTimeForAllJobs = 0

    def AddJob(self,newJob:Job):
        self.GetAllJobs().append(newJob)
        self._sumOfTimeForAllJobs = self._sumOfTimeForAllJobs + newJob.GetTime() # Upadte sum time of all jobs
    
    def HowManyJobs(self) -> int:
        return len(self._jobsArray)


    def GetAllJobs(self) -> list:
        return self._jobsArray
    
    def GetSumOfTimeForAllJobs(self) -> int:
        return self._sumOfTimeForAllJobs
    
    def copyJobsArray(self,newjobs:list):
        self._jobsArray = newjobs
    