import networkx as nx
import matplotlib.pyplot as plt

# Take user input
n = int(input("Enter number of vertices (greater than 3): "))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    # Create complete graph
    G = nx.complete_graph(n)

    # Draw graph
    pos = nx.circular_layout(G)  # Arrange in circle
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=800, edge_color='gray')

    plt.title(f"Complete Graph with {n} Vertices")
    plt.show()
