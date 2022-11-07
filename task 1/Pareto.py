#effective pareto


class Agent():

    """
    INPUT : the index of an option.
    OUTPUT: the value of the option to the agent
    """
    _OptionVal = {} # option-int : value-float
    
    def __init__(self):
      self._OptionVal = dict()

    # getter method
    def value(self, option:int) -> float:
        return self._OptionVal[option]
      
    # setter method
    def setOption(self, option:int, value:float):
        self._OptionVal[option] = value
   


def isParetoImprovement(agents:list, option1:int, option2:int)->bool:
    '''
    Description:
        A function that checks whether option 1 is a Pareto improvement of option 2
    Param :
        List of value agents
        option1(int) - An index that points to the attributed value of this option according to that agent
        option2(int) - An index that points to the attributed value of this option according to that agent
    Return:
        True - If option 1 is a detail improvement of option 2
        If there is at least one large value and all other values are equal or greater in option 1 than option 2
        Otherwise false
    '''
    #Denotes one or more agents option 1 gives it a higher value than option 2
    #True - Option 1 holds a higher value, False - Option 1 doesn't holds a higher value then 2
    flag = False
    for agent in agents :
        if agent.value(option1) < agent.value(option2):
            return False

        if agent.value(option1) > agent.value(option2):
            flag = True

        #elif : equals then nothing..

    if flag:
        return True #It is enough that one value is higher and all the others should be equal or higher
    
    return False # Because option1 and option2 have the same values in all agents




def isParetoOptimal(agents:list, option:int, allOptions:list)->bool:
    '''
    Description:
        A function that checks whether an option is Pareto efficient
    Param:
        List of value agents
    Return:
        True - If none of the other options is a Pareto improvement of the single option
        Otherwise false
    '''

    for LoopOption in allOptions:
        if isParetoImprovement(agents,LoopOption,option):
            return False
    
    return True

def isParetoImprovementTests():
    Ami = Agent()
    Tami = Agent()
    Rami = Agent()
    Ami.setOption(1,3)
    Ami.setOption(2,2)
    Tami.setOption(1,1)
    Tami.setOption(2,1)
    Rami.setOption(1,5)
    Rami.setOption(2,5)
    agents = [Ami,Tami,Rami]

    #Check isParetoImprovement function when option1 is ParetoImprovement of option2
    answerIsParetoImprovement = isParetoImprovement(agents,1,2)
    if answerIsParetoImprovement:
        print("pass answerIsParetoImprovement test")
    else:
        print("Falid answerIsParetoImprovement test")

    #Check isParetoImprovement function for Equals values options
    answerForEqualsOptions = isParetoImprovement(agents,1,1)
    if answerForEqualsOptions is False:
        print("pass answerForEqualsOptions test")
    else:
        print("Falid answerForEqualsOptions test")

    #Check isParetoImprovement function when option1 is not ParetoImprovement of option2
    Tami.setOption(1,0)
    answerIsNotParetoImprovement = isParetoImprovement(agents,1,2)
    if answerIsNotParetoImprovement is False:
        print("pass answerIsNotParetoImprovement test")
    else:
        print("Falid answerIsNotParetoImprovement test")

def isParetoOptimalTests():
    Ami = Agent()
    Tami = Agent()
    Rami = Agent()
    Ami.setOption(1,1)
    Ami.setOption(2,2)
    Ami.setOption(3,3)
    Ami.setOption(4,4)
    Ami.setOption(5,5)
    Tami.setOption(1,3)
    Tami.setOption(2,1)
    Tami.setOption(3,2)
    Tami.setOption(4,5)
    Tami.setOption(5,4)
    Rami.setOption(1,3)
    Rami.setOption(2,5)
    Rami.setOption(3,5)
    Rami.setOption(4,1)
    Rami.setOption(5,1)
    agents = [Ami,Tami,Rami]
    allOptions = [1,2,3,4,5]
    #check option1
    answerForOption1 = isParetoOptimal(agents,1,allOptions)
    if answerForOption1:
        print("pass answerForOption1 test")
    else:
        print("Falid answerForOption1 test")

    #check option2
    answerForOption2 = isParetoOptimal(agents,2,allOptions)
    if answerForOption2 is False:
        print("pass answerForOption2 test")
    else:
        print("Falid answerForOption2 test")

    #check option3
    answerForOption3 = isParetoOptimal(agents,3,allOptions)
    if answerForOption3:
        print("pass answerForOption3 test")
    else:
        print("Falid answerForOption3 test")

    #check option4
    answerForOption4 = isParetoOptimal(agents,4,allOptions)
    if answerForOption4:
        print("pass answerForOption4 test")
    else:
        print("Falid answerForOption4 test")

    #check option5
    answerForOption5 = isParetoOptimal(agents,5,allOptions)
    if answerForOption5:
        print("pass answerForOption5 test")
    else:
        print("Falid answerForOption5 test")


if __name__ == '__main__':
    isParetoImprovementTests()
    isParetoOptimalTests()


