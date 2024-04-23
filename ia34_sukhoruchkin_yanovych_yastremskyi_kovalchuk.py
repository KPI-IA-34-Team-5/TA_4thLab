from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight



def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    path_cost = shortest_paths[end][1]
    return path, path_cost


# Example input data:
input_matrix = [
            [0, 4 , 0, 0 , 0 , 0 , 0, 8 , 0],
            [4, 0 , 8, 0 , 0 , 0 , 0, 11, 0],
            [0, 8 , 0, 7 , 0 , 4 , 0, 0 , 2],
            [0, 0 , 7, 0 , 9 , 14, 0, 0 , 0],
            [0, 0 , 0, 9 , 0 , 10, 0, 0 , 0],
            [0, 0 , 4, 14, 10, 0 , 2, 0 , 0],
            [0, 0 , 0, 0 , 0 , 2 , 0, 1 , 6],
            [8, 11, 0, 0 , 0 , 0 , 1, 0 , 7],
            [0, 0 , 2, 0 , 0 , 0 , 6, 7 , 0]
        ]

def matrix_to_edges(inp_matrix):
    edges = []

    l = len(inp_matrix)
    for i in range(len(inp_matrix)):
        ii = inp_matrix[i]
        if len(ii) != l:
            raise Exception("Incorrect input was provided.")
        for j in range(len(ii)):
            jj = ii[j]
            if jj <= 0:
                continue
            edges.append((str(i), str(j), jj))
    return edges
        

graph = Graph()

for edge in matrix_to_edges(input_matrix):
    graph.add_edge(*edge)

# Example input data:
find_from = "3"
find_to = "7"
print(dijsktra(graph, find_from, find_to))