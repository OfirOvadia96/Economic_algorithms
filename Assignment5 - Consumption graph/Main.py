
import networkx as nx
import matplotlib.pyplot as plt
from Algorithms import *

if __name__ == '__main__':

    # Example 1: (with cycle)
    allocationMatrix = [[0.5,0,1,0.2],[0.5,1,0,0.8]]
    print_matrix(allocationMatrix)
    result1 = find_cycle_in_consumption_graph(allocationMatrix)
    print_cycle(result1[1])
    draw_graph(result1[0])

    # Example 2: (without cycle)
    allocationMatrix = [[0,0,1,0],[1,1,0,1]]
    print_matrix(allocationMatrix)
    result2 = find_cycle_in_consumption_graph(allocationMatrix)
    print_cycle(result2[1])
    draw_graph(result2[0])

    # Example 3: (with cycle)
    allocationMatrix = [[1,0.6,0,0,0.1],[0,0.3,0,1,0.3],[0,0.1,1,0,0.6]]
    print_matrix(allocationMatrix)
    result3 = find_cycle_in_consumption_graph(allocationMatrix)
    print_cycle(result3[1])
    draw_graph(result3[0])

    # Example 4: (without edges - negative matrix)
    allocationMatrix = [[-1,-0.6,-0,-0,-0.1],[-0,-0.3,-0,-1,-0.3],[-0,-0.1,-1,-0,-0.6]]
    print_matrix(allocationMatrix)
    result4 = find_cycle_in_consumption_graph(allocationMatrix)
    print_cycle(result4[1])
    draw_graph(result4[0])
    