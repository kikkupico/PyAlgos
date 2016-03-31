class DictGraph(object):
    def __init__(self):
        self.nodes = {}
    
    def create_from_dict(self,d):
        for node, links in d.items():
            self.nodes[node] = set(links)
            for linked_node in links:
                if linked_node not in self.nodes:
                    self.nodes[linked_node] = set()
    
    def depth_first_traverse(self, node, order):
        if node not in order:
           order.append(node)
         
           for linked_node in self.nodes[node]:
              self.depth_first_traverse(linked_node, order)
        
        return order
            
    def breadth_first_traverse(self, node, order):
        
        if node not in order:
            order.append(node)
        
        for linked_node in self.nodes[node]:
            if linked_node not in order:
                order.append(linked_node)
            
        for linked_node in self.nodes[node]:
            self.breadth_first_traverse(linked_node, order)
        
        return order
        
    def get_adjacency_matrix(self):
        size = len(self.nodes)
        adj_matrix = [[0 for x in range(0, size)] for x in range(0,size)]
        
        order = list(self.nodes.keys())
        order.sort()
        
        #debug 
        #print(order)
        
        for node, links in self.nodes.items():
            for link in links:
                adj_matrix[order.index(node)][order.index(link)] = 1
            
        return adj_matrix
        
    def __str__(self):
        return str(self.nodes)
    

if __name__ == "__main__":
    g = DictGraph()
    g.create_from_dict({"a":["b","c"],"b":["c"],"c":[]})
    print(g)
    print(g.get_adjacency_matrix())

        