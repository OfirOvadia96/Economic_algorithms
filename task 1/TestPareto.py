import unittest
from Pareto import Agent

class TestPareto(unittest.TestCase):

    
    def isParetoImprovementTest(self):
        setUpisParetoImprovementTest()
        self.assertEqual(0, 0)
    
    
    def isParetoOptimalTest(self):
        setUpisParetoOptimalTest()
        self.assertEqual(0, 0)


def setUpisParetoImprovementTest():
    Ami = Agent()
    Tami = Agent()
    agents = [Ami,Tami]

def setUpisParetoOptimalTest():
    Ami = Agent()
    Tami = Agent()
    Rami = Agent()
    agents = [Ami,Tami,Rami]

if __name__ == '__main__':
    unittest.main()