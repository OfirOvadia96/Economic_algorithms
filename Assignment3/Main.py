from Student import Student
from Job import Job
from Jobs import Jobs
from Students import Students
# import sys
import random
from Algorithms import GreedyAlgorithm
from Algorithms import ApproximationTotheOptimalTiming
import matplotlib.pyplot as plt

def OneProblem(NumberOfStudents:int ,NumberOfJobs:int) -> float:
    jobs = Jobs()
    students = Students()

    for i in range(NumberOfJobs):
        jobs.AddJob(Job(random.randint(1,100)))

    for i in range(NumberOfStudents):
        students.AddStudent(Student())
    
    GreedyAlgorithm(jobs,students)
    return ApproximationTotheOptimalTiming(jobs,students)

if __name__ == '__main__':
    RandomProblemsResults = []
    RandomNumberOfJobsList = []
    studentList = [2,3,4]
    for problem in studentList:
        NumberOfJobs = random.randint(1,100)
        RandomProblemsResults.append(OneProblem(problem,NumberOfJobs))
        RandomNumberOfJobsList.append(NumberOfJobs)

    plt.plot(studentList,RandomProblemsResults)
    plt.show()



        
    