class Vertex(object):
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Vertex(name))
        return self
