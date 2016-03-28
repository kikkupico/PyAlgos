class GraphNode(object):
    def __init__(self, label):
        self.label = label
        self.links = set()

    def add_links(self, links):
        if( type(links) != set ):
            links = set(links)
            for link in links:
                if type(link) != GraphNode:
                    raise TypeError
            self.links = links
    
    def add_link(self, link):
        if type(link) != GraphNode:
            raise TypeError
        else:
            self.links.add(link)
            
    def __hash__(self):
        return hash(self.label)
    
    def __eq__(self,other):
        return self.label == other.label

    def __str__(self):
        output_string = "Node: " + self.label + " Links: " + str(self.links)
        return output_string
        
    def __repr__(self):
        return self.label
    
    
class Graph(object):
    def __init__(self):
        self.nodes = set()
        
    def create_from_dict(self, d):
        for nodelabel, linklabels in d.items():
            n = GraphNode(nodelabel)
            self.nodes.add(n)
            for linklabel in linklabels:
                linknode = GraphNode(linklabel)
                n.links.add(linknode)
                if linknode not in self.nodes:
                    self.nodes.add(linknode)

    def add_node(self, label, links):
        n = GraphNode(label)
        n.add_links(links)
        self.nodes.add(n)
        
        for node in links:
            if node not in self.nodes:
                self.nodes.add(node)

        
    def __str__(self):
        output_string = ""
        for node in self.nodes:
            output_string = output_string + "\n" + str(node)
        return output_string

if __name__ == "__main__":
    g = Graph()
    g.create_from_dict({"a":["b","c"],"b":["c"]})
    #g.nodes.add(GraphNode("d"))
    print(g)