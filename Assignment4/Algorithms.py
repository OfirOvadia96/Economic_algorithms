

def SumOfValues(arrayOfValues):
    '''Param: List of player values
       Retrun: Sum of values'''

    sum = 0
    for value in arrayOfValues:
        sum = sum + value
    return sum


def CheckDivisions(divisionPlayer1:list,divisionPlayer2:list):
    if len(divisionPlayer1) != len(divisionPlayer2):
        return False
    
    index = 0
    while index < len(divisionPlayer1):
        sum = divisionPlayer1[index] + divisionPlayer2[index]
        if sum != 1:
            print("Error!, Object distribution greater than 100%")
            return False
        index = index + 1

    return True
        

def CheckPlayersValues(player1Values:list,player2Values:list):
    
    if len(player1Values) !=  len(player2Values):
        return False
    
    sumValPlayer1 = SumOfValues(player1Values)
    sumValPlayer2 = SumOfValues(player2Values)
    if sumValPlayer1 != sumValPlayer2:
        print("Error!, The sum of the values of the players is not equal. It is necessary to normalize the values")
        return False
    
    return True


def CheckingValidation(player1Values:list,player2Values:list,divisionPlayer1:list,divisionPlayer2:list):
    validPlayers = CheckPlayersValues(player1Values,player2Values)
    validDivisions = CheckDivisions(divisionPlayer1,divisionPlayer2)
    
    if validPlayers and validDivisions:
        return True
    #else:
    return False


def ValuesRatioCalculate(vectorValPlayer1:list, vectorValPlayer2:list):
    valuesRatio = []
    index = 0
    while index < len(vectorValPlayer1):
        valuesRatio.append(vectorValPlayer1[index]/vectorValPlayer2[index])
    return valuesRatio


def Organized(player1Values : list, player2Values: list, divisionPlayer1:list, divisionPlayer2:list) ->bool:
    
    valid = CheckingValidation(player1Values,player2Values,divisionPlayer1,divisionPlayer2)
    if not valid:
        return
    

    answer = True
    valuesRatio = ValuesRatioCalculate(player1Values,player2Values)
    
    index = 0
    innerIndex = 0
    while index < len(divisionPlayer1):
        
        if divisionPlayer1[index] == 0 : # Definitely happens together with the first condition: divisionPlayer2[index] == 1
            valRatioPlayer2 = valuesRatio[index]
            while innerIndex < len(player1Values):
                if player1Values[innerIndex] > 0:
                    if valRatioPlayer2 > valuesRatio[index]:
                        ''' A value is found in player2 basket of values         
                            that is greater than a number in player1 basket of values'''
                        answer = False # The division is not arranged
                        break                    
                innerIndex = innerIndex + 1
            
            innerIndex = 0

    if answer:
        print("Yes")
    else:
        TheCorrectedConductor(player1Values,player2Values)
    
    return


def TheCorrectedConductor(player1Values:list, player2Values:list):
    print("The given division is not an orderly division ! ")
    print("Division after pareto improvement:")
    newDivisionPlayer1 = []
    newDivisionPlayer2 = []
    
    
    # TODO: Sort the lists of values ​​according to the ratio of values
    #*****************************************************************************

    #init values according to the algorithm settings - give all to player1
    index = 0
    sumOfValuesPlayer1 = 100
    sumOfValuesPlayer2 = 0
    while index < len(player1Values):
        newDivisionPlayer1.append(1)
        newDivisionPlayer2.append(0)
        index = index + 1


    index = 0
    while index < len(player1Values):
        #give player2 1 item
        newDivisionPlayer1[index] = 0
        newDivisionPlayer2[index] = 1
        sumOfValuesPlayer1 = sumOfValuesPlayer1 - player1Values[index]
        sumOfValuesPlayer2 = sumOfValuesPlayer2 + player1Values[index]
        if sumOfValuesPlayer1 == sumOfValuesPlayer2:
            break
        
        elif sumOfValuesPlayer1 < sumOfValuesPlayer2:
            # TODO: need to divied item
            DiviedItem()
            break
        
        index = index + 1

    
    print("Pareto improvement: ")
    print("Division player1:")
    print( "[" , *player1Values , "]")
    print("Division player2:")
    print( "[" , *player2Values , "]")

    # TODO: Calculate what changed from the other division to see how its pareto improvment
    ##****************************

    return