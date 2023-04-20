import sys
#from udacity
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        print("relaxed: Vertex ", unvisited_nodes, "Infinty paths: ",shortest_path)
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "s", "t"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# init_graph["A"]["B"] = 4
# init_graph["A"]["C"] = 2
# init_graph["B"]["D"] = 2
# init_graph["B"]["C"] = 3
# init_graph["C"]["B"] = 1
# init_graph["C"]["D"] = 4
# init_graph["E"]["D"] = 1
init_graph["s"]["A"] = 1
init_graph["s"]["G"] = 6
init_graph["s"]["D"] = 4
init_graph["A"]["B"] = 2
init_graph["A"]["E"] = 2
init_graph["B"]["C"] = 2
init_graph["C"]["t"] = 4
init_graph["D"]["E"] = 3
init_graph["G"]["D"] = 2
init_graph["G"]["E"] = 1
init_graph["G"]["H"] = 6
init_graph["E"]["C"] = 2
init_graph["E"]["F"] = 3
init_graph["E"]["I"] = 3
init_graph["D"]["A"] = 3
init_graph["F"]["C"] = 1
init_graph["F"]["t"] = 3
init_graph["I"]["F"] = 1
init_graph["I"]["t"] = 1
init_graph["H"]["E"] = 2
init_graph["H"]["I"] = 6



graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="s")
print_result(previous_nodes, shortest_path, start_node="s", target_node="t")
for k, v in shortest_path.items():
    print("Node (",k,") with Weight:", v, " is added to the 'visited'")


# make change from geeksforgeeks.com
def findMin(V):
    v = V
    # All denominations of Indian Currency
    deno = [.01, .05, .1, .25, .5, 1, 5, 10, 20, 50,
            100]
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while (i >= 0):

        # while V is still greater than denominations keep going
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i -= 1
    # Print result
    for i in range(len(ans)):
        print(ans[i], end=" ")

    # count how many forms of change that can be made
    # use lower number than 269.63 because it takes a few minutes to find all permutations
    nchanges = []

    def changes(ans, v, newchange=[]):
        if sum(newchange) == v:
            nchanges.append(newchange)
            return
        if sum(newchange) > v:
            return
        for i in ans:
            # add found new change form to new list
            changes(ans, v, newchange+[i])
        return nchanges
    print(changes(ans, v), "\nWays to make change: ", len(nchanges))

n = 369.63
# to make findMin fail
# n = -12
print(n, ": ", end="")
findMin(n)
