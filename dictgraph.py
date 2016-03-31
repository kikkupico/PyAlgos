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
        
        #ASSUMPTION 1: distance from node to itself is 0 if not defined
        #ASSUMPTION 2: distance from node to any other node is infinity if not defined
        
        size = len(self.nodes)
        adj_matrix = [[float('infinity') for x in range(0, size)] for x in range(0,size)]
        
        for i in range(0,size):
            adj_matrix[i][i] = 0
        
        order = list(self.nodes.keys())
        order.sort()
        
        #debug 
        #print(order)
        
        for node, links in self.nodes.items():
            for link in links:
                adj_matrix[order.index(node)][order.index(link)] = 1
            
        return adj_matrix
        
    def __str__(self):
        output =""
        order = list(self.nodes.keys())
        order.sort()
        
        for node in order:
            output += "Node:{0} Links:{1}\n".format(str(node),str(self.nodes[node]))
        return output
    

if __name__ == "__main__":
    g = DictGraph()
    g.create_from_dict({"a":["b","c"],"b":["c"],"c":[]})
    print(g)
    print(g.get_adjacency_matrix())
