# Depth First Search
"""
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a
simple tree-like structure. Implement the depthFirstSearch method on the Node class, which takes in an empty array,
traverse the tree using the Depth-first Search approach(specifically navigating form left to right), stores all the
Node's names in the input array, and returns it.
"""
from datastructures.grah import Vertex


class Node(Vertex):
    def depthFirstSearch(self, array):
        childs = self.children[::-1]  # gonna use list as a stack
        array.append(self.name)
        while childs:
            child = childs.pop(-1)  # last in first out
            grand_children = child.children

            array.append(child.name)
            if grand_children:
                childs.extend(grand_children[::-1])

        return array
