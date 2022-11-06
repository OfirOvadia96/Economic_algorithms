#effective pareto


class Agent():

     """
    INPUT : the index of an option.
    OUTPUT: the value of the option to the agent
    """
    OptionVal = {} # option-int : value-float
   

def isParetoImprovement(agents:List[],option1:int,option2:int)->bool:
    #Denotes one or more agents option 1 gives it a higher value than option 2
    #True - Option 1 holds a higher value, False - Option 1 doesn't holds a higher value then 2
    flag = false
    for(agent in agents):
        if(agent.OptionVal[option1] < agent.OptionVal[option2]):
            return False

        if(agent.OptionVal[option1] > agent.OptionVal[option2])
            flag = True

        #elif : equals then nothing..

    if(flag):
        return True #It is enough that one value is higher and all the others should be equal or higher
    
    return False # Because option1 and option2 have the same values in all agents





def isParetoOptimal(agents:List[Agent], option:int, allOptions:List[int])->bool:
    