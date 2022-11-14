from Party import Party

class Country():

    def __init__(self,NumberOfSeatsInKnesset:int = 120):
        self.partysState = []
        self.numberOfSeatsInKnesset = NumberOfSeatsInKnesset


    def AddParty(self,party:Party):
        self.partysState.append(party)


    #return index Party with the highest votes
    def MostDivisionQuotient(self) -> Party:
        highestDivisionQuotient = 0
        ThePartyIndex = 0
        for x in range(len(self.partysState)):
            if highestDivisionQuotient < self.partysState[x].GetDivisionQuotient():
                highestDivisionQuotient = self.partysState[x].GetDivisionQuotient()
                ThePartyIndex = x

        return self.partysState[ThePartyIndex]


    def PrintReasults(self):
        for x in self.partysState:
            print(x.name , ": " , x.seats)

    #Jefferson's algorithm using Webster's method
    def Jefferson_Algorithm(self):
        if len(self.partysState):
            #list is not empty
            i = 0
            while(i < self.numberOfSeatsInKnesset):
                PartyWithHighestNumberOfVotes = self.MostDivisionQuotient()
                PartyWithHighestNumberOfVotes.GiveSeat()
                i = i + 1

        else:
            print("Error!, there is no Partys in this Country")

