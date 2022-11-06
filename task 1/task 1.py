#effective pareto


class Agent():

     """
    INPUT : the index of an option.
    OUTPUT: the value of the option to the agent
    """
    OptionVal = {} # option-int : value-float
   


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
    flag = false
    for agent in agents :
        if agent.OptionVal[option1] < agent.OptionVal[option2]:
            return False

        if agent.OptionVal[option1] > agent.OptionVal[option2]:
            flag = True

        #elif : equals then nothing..

    if flag:
        return True #It is enough that one value is higher and all the others should be equal or higher
    
    return False # Because option1 and option2 have the same values in all agents




def isParetoOptimal(agents:list, option:int, allOptions:list)->bool:
    '''
    Description:
    A function that checks whether an option is Pareto efficient
    
    '''

    for LoopOption in allOptions:
        if isParetoImprovement(agents,LoopOption,option):
            return False
    
    return True
