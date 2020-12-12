def sort(graph, n):
    """
    Concept:
    what is early activity time for an activity?
        the time an activity can start as soon as an event occured which inturn means all of the activities makes that event should be 
        completed(simply max time taken of all the prceeding activites to be completed) 
    
    find early activity time for each activity
    1. use topsort so that all preceeding for that particular vertex will be completed first
    2. formula :
        for edge/activity <k,l> , i-th activity
        e(i) = ee[k]

        ee[k] = max([ee[i] + duration of<i,j> for i in predecessor of j])

    problem:
        no way to accesss the predecessor easily in adjacency list representation
        soln - keep addional array and compute the ee[k] on each vertex for next vertex
        
        ee[4] will be found while processing both
            graph.add_edge(1, 4, 1) 
            graph.add_edge(2, 4,5) 

    Implementation Details:
    """
    print("Topological Order is")
    ee = [0 for i in range(n)]
    top = -1
    for k,v  in graph.count.items():
        if v == 0:
            graph.count[k] = top
            top = k
    
    for i in range(n):
        if top == -1:
            print("Graph contain cycles. Can't proceed")
            break
        else:
            temp = top
            print(temp, end=", ")
            top = graph.count[temp]
            
            ptr = graph.graph[temp]
            while ptr:
                k = ptr.vertex
                # update ee[]
                # if ptr.next:
                #     if (ee[ptr.next.vertex] < ee[k]+ ptr.duration):
                #         ee[ptr.next.vertex] = ee[k]+ ptr.duration
                if ee[ptr.vertex] < ee[temp]+ptr.duration:
                    ee[ptr.vertex] = ee[temp]+ptr.duration
                graph.count[k] -= 1
                if graph.count[k] == 0:
                    #  update count and top
                    graph.count[k] = top
                    top = k
                ptr = ptr.next
    print("\n\n")
    print(ee)

""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""
  
# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
        self.duration = 0
  
  
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
    def add_edge(self, src, dest, duration): 
        # Adding the node to the source node         
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        node.duration = duration
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
    V = 9
    graph = Graph(V) 
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 2, 4) 
    graph.add_edge(0, 3, 5)

    graph.add_edge(1, 4, 1) 
    
    graph.add_edge(2, 4, 1) 
    

    graph.add_edge(3, 5, 2) 
    
    graph.add_edge(4, 6, 9) 
    graph.add_edge(4, 7, 7) 

    graph.add_edge(5, 7, 4)

    graph.add_edge(6, 8, 2)

    graph.add_edge(7, 8, 4)
  
    graph.print_graph() 
    

    sort(graph, V)
