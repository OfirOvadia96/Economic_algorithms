import unittest
from Pareto import Agent
from Pareto import isParetoImprovement
from Pareto import isParetoOptimal

class TestPareto(unittest.TestCase):

    
    def isParetoImprovementTest(self):
        # agents = setUpisParetoImprovementTest()
        # answer = isParetoImprovement(agents,1,2)
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
        answer = isParetoImprovement(agents,1,2)
        if(answer):
            print("good")
        self.assertTrue(answer)

        

    
    
    # def isParetoOptimalTest(self):
    #     setUpisParetoOptimalTest()
    #     self.assertEqual(0, 0)


# def setUpisParetoImprovementTest() -> list:
#     Ami = Agent()
#     Tami = Agent()
#     Rami = Agent()
#     Ami.setOption(1,3)
#     Ami.setOption(2,2)
#     Tami.setOption(1,1)
#     Tami.setOption(2,1)
#     Rami.setOption(1,5)
#     Rami.setOption(2,5)
#     agents = [Ami,Tami,Rami]
#     return agents

# def setUpisParetoOptimalTest():
#     Ami = Agent()
#     Tami = Agent()
#     Rami = Agent()
#     agents = [Ami,Tami,Rami]

if __name__ == '__main__':
    unittest.main()