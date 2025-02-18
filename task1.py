import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def create_graph():
    G = nx.DiGraph()
    
    edges = [
        ('T1', 'S1', 25), ('T1', 'S2', 20), ('T1', 'S3', 15),
        ('T2', 'S3', 15), ('T2', 'S4', 30), ('T2', 'S2', 10),
        ('S1', 'M1', 15), ('S1', 'M2', 10), ('S1', 'M3', 20),
        ('S2', 'M4', 15), ('S2', 'M5', 10), ('S2', 'M6', 25),
        ('S3', 'M7', 20), ('S3', 'M8', 15), ('S3', 'M9', 10),
        ('S4', 'M10', 20), ('S4', 'M11', 10), ('S4', 'M12', 15),
        ('S4', 'M13', 5), ('S4', 'M14', 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    return G

def compute_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)

def analyze_results(flow_dict):
    result = []
    for source, destinations in flow_dict.items():
        for dest, flow in destinations.items():
            if flow > 0:
                result.append([source, dest, flow])
    return pd.DataFrame(result, columns=['Терминал/Склад', 'Магазин', 'Фактический Поток'])

def visualize_graph(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'capacity')
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Логистическая сеть")
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    
    G.add_edge('Source', 'T1', capacity=100)
    G.add_edge('Source', 'T2', capacity=100)
    G.add_edge('M1', 'Sink', capacity=100)
    G.add_edge('M2', 'Sink', capacity=100)
    G.add_edge('M3', 'Sink', capacity=100)
    G.add_edge('M4', 'Sink', capacity=100)
    G.add_edge('M5', 'Sink', capacity=100)
    G.add_edge('M6', 'Sink', capacity=100)
    G.add_edge('M7', 'Sink', capacity=100)
    G.add_edge('M8', 'Sink', capacity=100)
    G.add_edge('M9', 'Sink', capacity=100)
    G.add_edge('M10', 'Sink', capacity=100)
    G.add_edge('M11', 'Sink', capacity=100)
    G.add_edge('M12', 'Sink', capacity=100)
    G.add_edge('M13', 'Sink', capacity=100)
    G.add_edge('M14', 'Sink', capacity=100)
    
    max_flow_value, flow_dict = compute_max_flow(G, 'Source', 'Sink')
    
    df_results = analyze_results(flow_dict)
    print(df_results)
    df_results.to_csv("logistics_flow_results.csv", index=False)
    print("Результаты сохранены в logistics_flow_results.csv")
    
    visualize_graph(G)
    
    print(f"Максимальный поток: {max_flow_value}")
