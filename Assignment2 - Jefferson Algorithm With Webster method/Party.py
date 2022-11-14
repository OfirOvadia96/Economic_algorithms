
class Party():
    
    def __init__(self,Name = "", Votes:int = 0, Seats:int = 0, Divider:float = 0):
        self.name = Name
        self.votes = Votes 
        self.seats = Seats #The current number of seats for that party
        self.divider = Divider
        self.divisionQuotient = Votes #Determines who will be given the next seat
    

    def GetVotes(self) -> int:
        return self.votes
    

    def GetSeats(self) -> int:
        return self.seats
    

    def SetSeats(self,Seats:int):
        self.seats = Seats
    

    def IncreaseSeats(self):
        self.seats = self.seats + 1


    # Webster's method
    def UpdateDivider(self):
        self.divider = self.seats + 0.5


    def GetDivisionQuotient(self)->int:
        return self.divisionQuotient


    def UpdateDivisionQuotient(self):
        self.divisionQuotient = self.votes/self.divider


    def GiveSeat(self):
        self.UpdateDivider()
        self.UpdateDivisionQuotient()
        self.IncreaseSeats()
