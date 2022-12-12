import networkx as nx
import matplotlib.pyplot as plt


def PrintMatrix(pricing_matrix:list[list]):
    '''Print the pricing matrix'''
    for row in pricing_matrix:
        print(row)
    print("")


def draw_given_graph(graph:nx.Graph):
    options = {
    "font_size": 8,
    "node_size": 100,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
    }
    
    nx.draw_networkx(graph,None,True,**options)
    ax = plt.gca()
    ax.margins(0.000001)
    plt.axis("off")
    plt.show()


def draw_egletre_graph(G:nx.Graph):
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]

    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=400)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.000001)
    plt.axis("off")
    plt.tight_layout()
    plt.show()




def Finding_egalitarian_division(list_of_divisions:list[nx.Graph],rooms_names:list[str],Tenants_names:dict[str],
        how_much_was_the_price:dict):
        
    benefit = 0
    lowest_benefits = []

    for index in range(len(list_of_divisions)):
        tenant_with_the_lowest_benefit_in_the_division = 9999999

        for room_name in rooms_names:
            for Tenant_name in Tenants_names:
                weight = list_of_divisions[index].get_edge_data(room_name,Tenant_name)
                if weight is not None:
                    benefit = how_much_was_the_price[room_name] - weight["weight"] # how much is the value pricing - how much actually paid
                    if tenant_with_the_lowest_benefit_in_the_division > benefit:
                        tenant_with_the_lowest_benefit_in_the_division = benefit

        lowest_benefits.append(tenant_with_the_lowest_benefit_in_the_division)
    

    graph_index = -1
    number = 999999
    for i in range(len(lowest_benefits)):
        if lowest_benefits[i] < number:
            number = lowest_benefits[i]
            graph_index = i




    return list_of_divisions[graph_index]