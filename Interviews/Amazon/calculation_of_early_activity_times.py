import math

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
        e(i) = ee[k] and l(i) = le(l) - duration of the activity
        
        expanded formula:
        
        ee[k] = max([ee[i] + duration of<i,j> for i in predecessor of j])

        le(l) = min([le[i] - duration of<j,i> for each adjacent(sucessor) vertex of j ])
 
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
    top_sorted = []
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
            top_sorted.append(temp)

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
    return top_sorted, ee


def get_le(top_sorted,graph, V, le, ee):
    top_sorted.reverse()
    print(top_sorted)
    le = [math.inf for i in ee]
    le[-1] = ee[-1]
    for event in top_sorted:
        print("event", event)
        sucessor =  graph.graph[event]
        while sucessor:
            print("sucessor", sucessor.vertex, sucessor.duration,le[sucessor.vertex] ,le[event] ,le[sucessor.vertex] - sucessor.duration < le[event])
            if le[sucessor.vertex] - sucessor.duration < le[event]:
                le[event] = le[sucessor.vertex] - sucessor.duration
            # print(sucessor.vertex)         
            sucessor = sucessor.next
        print("\n")
    print("le out",le)
    return le

def get_e_and_l(ee, le, graph):
    e = []
    l = []
    for node, adj in enumerate(graph.graph):
        print("node", node)        
        while adj:
            print("adj",adj.vertex)
            e.append(ee[node])
            print("le[adj.vertex], adj.duration",le[adj.vertex], adj.duration)
            l.append(le[adj.vertex] - adj.duration)
            adj = adj.next
    return e,l

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
    

    top_sorted, ee = sort(graph, V)
    le = ee
    le = get_le(top_sorted, graph, V, le, ee)
    print("le out",le)
    e,l = get_e_and_l(ee, le, graph)
    print("e",e,"l",l)
    print("l-e or slack")
    for e,l in zip(e,l):
        print(l-e, end="-")
        if l-e ==0:
            print("YES")
        else:
            print("NO")
        print("\n")
