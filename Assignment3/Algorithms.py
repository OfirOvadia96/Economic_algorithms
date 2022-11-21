from Student import Student
from Job import Job
from Jobs import Jobs
from Students import Students
import sys
#from Job import comparator

# Division Of Work For Students
def GreedyAlgorithm(jobs:Jobs,students:Students):
    jobs.copyJobsArray(sorted(jobs.GetAllJobs(),reverse=True))

    for job in jobs.GetAllJobs():
        student = students.GetStudentWithMinTimeSumJobs()
        student.AddToWorkingTime(job)

# Finish time out of the greedy algorithm
def GetBiggestTimeForStudents(students:Students):
    biggestTime = students.GetAllStudents()[0].GetTimeJobs()
    for student in students.GetAllStudents():
        if biggestTime < student.GetTimeJobs():
            biggestTime = student.GetTimeJobs()
    return biggestTime


def GetBiggestTimeForJobs(jobs:Jobs):
    biggestTime = jobs.GetAllJobs()[0].GetTime()
    for job in jobs.GetAllJobs():
        if biggestTime < job.GetTime():
            biggestTime = job.GetTime()
    return biggestTime


# optimal time
def OptimalFinishTime(jobs:Jobs,students:Students) -> float:
    if students.GetAmountOfStudent() >= len(jobs.GetAllJobs()):
        return GetBiggestTimeForJobs(jobs)
    return jobs.GetSumOfTimeForAllJobs() / students.GetAmountOfStudent()

# Approximation to optimal
def ApproximationTotheOptimalTiming(jobs:Jobs,students:Students) -> float:
    return GetBiggestTimeForStudents(students) / OptimalFinishTime(jobs,students)


    

