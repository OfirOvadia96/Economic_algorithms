import unittest
import Pareto
from Pareto import Agent
from Pareto import isParetoImprovement
from Pareto import isParetoOptimal

def setUptestIsParetoImprovement()->list:
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
    return agents

def setUpisParetoOptimalTests():
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
    return agents,allOptions

class TestAdd(unittest.TestCase):

    ### Tests for isParetoImprovement function ###
    def test1IsParetoImprovement(self):
        agents = setUptestIsParetoImprovement()
        
        #Check isParetoImprovement function when option1 is ParetoImprovement of option2
        answerIsParetoImprovement = isParetoImprovement(agents,1,2)
        self.assertTrue(answerIsParetoImprovement)
    

    def test2IsParetoImprovement(self):
        agents = setUptestIsParetoImprovement()
        
        #Check isParetoImprovement function for Equals values options
        answerForEqualsOptions = isParetoImprovement(agents,1,1)
        self.assertFalse(answerForEqualsOptions)
    
    
    def test3IsParetoImprovement(self):
        agents = setUptestIsParetoImprovement()
        Ofir = Agent()
        Ofir.setOption(1,0)
        Ofir.setOption(2,1)
        #Check isParetoImprovement function when option1 is not ParetoImprovement of option2
        agents[1] = Ofir
        answerIsNotParetoImprovement = isParetoImprovement(agents,1,2)
        self.assertFalse(answerIsNotParetoImprovement)
    

    ### Tests for isParetoOptimal function ###
    def test1isParetoOptimalTests(self):
        agents, allOptions = setUpisParetoOptimalTests()
        #check for option1
        answerForOption1 = isParetoOptimal(agents,1,allOptions)
        self.assertTrue(answerForOption1)


    def test2isParetoOptimalTests(self):
        agents, allOptions = setUpisParetoOptimalTests()
        #check for option2
        answerForOption2 = isParetoOptimal(agents,2,allOptions)
        self.assertFalse(answerForOption2)


    def test3isParetoOptimalTests(self):
        agents, allOptions = setUpisParetoOptimalTests()
        #check for option3
        answerForOption3 = isParetoOptimal(agents,3,allOptions)
        self.assertTrue(answerForOption3)


    def test4isParetoOptimalTests(self):
        agents, allOptions = setUpisParetoOptimalTests()
        #check for option4
        answerForOption4 = isParetoOptimal(agents,4,allOptions)
        self.assertTrue(answerForOption4)


    def test5isParetoOptimalTests(self):
        agents, allOptions = setUpisParetoOptimalTests()
        #check for option5
        answerForOption5 = isParetoOptimal(agents,5,allOptions)
        self.assertTrue(answerForOption5)
    

if __name__ == '__main__':
    unittest.main()