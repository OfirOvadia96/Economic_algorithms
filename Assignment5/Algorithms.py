
import networkx as nx
import matplotlib.pyplot as plt

def build_graph(allocation:list[list[float]]):
    graph = nx.Graph()

    #players names
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Add players to graph
    for i in range(len(allocation)):
        graph.add_node(abc[i])

    # Add items to graph
    for i in range(len(allocation[0])):
        graph.add_node(i)

    # Add edges to graph
    for row in range(len(allocation)):
        for column in range(len(allocation[row])):
            if allocation[row][column] > 0:
                graph.add_edge(abc[row],column)

    return graph


def draw_graph(graph):
    options = {
    "font_size": 15,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 3,
    "width": 3,
    }
    
    nx.draw_networkx(graph,None,True,**options)
    plt.axis("off")
    plt.show()


def find_cycle_in_consumption_graph(allocation:list[list[float]]):
    graph = build_graph(allocation)
    try:
        cycle = nx.find_cycle(graph)

    except:
        cycle = "no cycle was found"

    return graph,cycle


def print_cycle(cycle:list):
    '''if cycle exists - print one cycle from the graph
        otherwise print "no cycle was found"'''

    if type(cycle) is list:
        for pair in cycle:
            print(pair[0],end = "->")

        print(cycle[0][0])
    else:
        print(cycle)
    
    print("")
    return


def print_matrix(matrix):
    '''Print the allocation matrix'''
    for row in matrix:
        print(row)
    print("")
