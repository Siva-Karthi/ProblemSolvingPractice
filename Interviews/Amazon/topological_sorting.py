def sort(graph, n):
    """
    Concept:
    1.Get the node with no predecessor 
    2.Delete that along with its out going edges

    Implementation Details:
    """
    top = -1
    for k,v in graph.count.items():
        if v == 0: # no predecessor
            if top == -1:
                graph.count[k] = 0
            else:
                graph.count[k] = top
            top = k
  
    for i in range(n):
        if top == -1:
            print("cyclic graph can't proceed")
        else:
            print("top", top)

            temp = graph.graph[top]

            print(temp.vertex)

            top = graph.count[top]
            print("next top", top)
            ptr = temp.next
            while ptr:
                k = ptr.vertex 
                if graph.count[k] == 0:
                    graph.count = top
                    top = k
                ptr = ptr.next

""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""
  
# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V
        self.count = {v:0 for v in range(vertices)}
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node         
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node
        try:
            self.count[dest] += 1
        except KeyError:
            self.count[dest] = 1
  
        # # Adding the source node to the destination as 
        # # it is the undirected graph 
        # node = AdjNode(src) 
        # node.next = self.graph[dest] 
        # self.graph[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="")             
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            else:
                print("->",0)
            print(" \n") 
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 6
    graph = Graph(V) 
    graph.add_edge(0, 1)
    graph.add_edge(0, 2) 
    graph.add_edge(0, 3) 

    graph.add_edge(1, 4) 
    
    graph.add_edge(2, 4) 
    graph.add_edge(2, 5) 

    graph.add_edge(3, 4) 
    graph.add_edge(3, 5) 
  
    graph.print_graph() 
    print(graph.graph)
    print(graph.count)

    sort(graph, V)