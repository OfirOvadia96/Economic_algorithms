from Algorithms import *

if __name__ == '__main__':
    # Construct an empty graph:
    # graph=nx.Graph()

    # # Add edges with weights:
    # graph.add_edge('aya','martef' ,weight=2)
    # graph.add_edge('aya','heder',weight=40)
    # graph.add_edge('aya','salon' ,weight=35)

    # graph.add_edge('batya','martef' ,weight=40)
    # graph.add_edge('batya','heder',weight=3)
    # graph.add_edge('batya','salon' ,weight=35)

    # graph.add_edge('gila','martef' ,weight=20)
    # graph.add_edge('gila','heder',weight=40)
    # graph.add_edge('gila','salon' ,weight=4)

    # print("Maximum-value matching: ", nx.max_weight_matching(graph))

    # division = nx.max_weight_matching(graph)
    # print(division)

    # Example
    # Pricing table:
    pricing_matrix_example = [[40,30,40]
              ,[30,30,80]
              ,[20,10,60]]
    PrintMatrix(pricing_matrix_example)

    how_much_was_the_price = {"Bed room":40,
                              "basement":90,
                              "Living room":60}

    # Constructing a graph of the maximum sum of values (not egalitarian)
    graph1 = nx.Graph()
    graph1.add_edge('Aya','Bed room' ,weight=40)
    graph1.add_edge('Batia','basement',weight=80)
    graph1.add_edge('Gila','Living room' ,weight=10)

    draw_given_graph(graph1)

    # Constructing a graph of the maximum sum of values (egalitarian)
    graph2 = nx.Graph()
    graph2.add_edge('Aya','Bed room' ,weight=40)
    graph2.add_edge('Batia','Living room',weight=30)
    graph2.add_edge('Gila','basement' ,weight=60)
    
    draw_given_graph(graph2)

    # Constructing a graph of the maximum sum of values (egalitarian)
    graph3 = nx.Graph()
    graph3.add_edge('Aya','Living room' ,weight=30)
    graph3.add_edge('Batia','basement',weight=80)
    graph3.add_edge('Gila','Bed room' ,weight=20)

    draw_given_graph(graph3)

    Tenants_names = ['Aya','Batia','Gila']
    rooms_names = ['Bed room','Living room','basement']
    list_of_divisions = [graph1,graph2,graph3]

    division_graph = Finding_egalitarian_division(list_of_divisions,rooms_names,Tenants_names,how_much_was_the_price)

    draw_egletre_graph(division_graph)



