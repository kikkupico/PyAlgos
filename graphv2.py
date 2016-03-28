class Graph(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes.add(name)
        
    def add_directed_link(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.directed_links.add((node1,node2))
        else:
            raise ValueError
            
    def __str__(self):
        return "Nodes: "+ str(self.nodes) + " Directed Links: "+ str(self.directed_links)
            
if __name__ == "__main__":
    g = Graph()
    g.add_node("a")
    g.add_node("b")
    g.add_directed_link("a","b")
    print(g)
    