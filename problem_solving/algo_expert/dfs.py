# Depth First Search
"""
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a
simple tree-like structure. Implement the depthFirstSearch method on the Node class, which takes in an empty array,
traverse the tree using the Depth-first Search approach(specifically navigating form left to right), stores all the
Node's names in the input array, and returns it.
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

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
