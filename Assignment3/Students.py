from Student import Student
from Job import Job
from Jobs import Jobs
import sys

class Students:

    def __init__(self):
        self._StudentsArray = [] # contatin Students objects

    def GetAllStudents(self) -> list:
        return self._StudentsArray

    def GetAmountOfStudent(self) -> int:
        return len(self._StudentsArray)
    
    
    def AddStudent(self,newStudent:Student):
        self._StudentsArray.append(newStudent)


    def GetStudentWithMinTimeSumJobs(self) -> Student:
        index = 0
        lowestSum = sys.maxsize
        location = 0 # Save the place of the student that have the lowest _sumOfTimeForJobs

        while index < len(self._StudentsArray):

            if lowestSum > self._StudentsArray[index].GetTimeJobs():
                lowestSum = self._StudentsArray[index].GetTimeJobs()
                location = index

            index = index + 1
    
        return self._StudentsArray[location]