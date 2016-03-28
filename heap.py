class Heap(object):
    def __init__(self, min_or_max):
        self.elements = []
        if min_or_max == "min" or min_or_max == "max":
            self.TYPE = min_or_max
        else:
            print("Heap type not recognized")
            return NotImplemented
    
    def create_from_list(self, n):
        for i in range(0,len(n)):
            self.elements.append(n[i])
            
            #debug
            #print(self.elements)
            
            self.heapify(len(self.elements)-1)
    
    def heapify(self, n):
        if n == 0:
            return
        
        if n%2 == 0: #if n is even
            parent = int((n-2)/2)
        else:
            parent = int((n-1)/2) #if n is odd
        
        #debug
        #print("n:{0},parent{1}".format(n,parent))
        
        if self.TYPE == 'max':
            if self.elements[parent]<self.elements[n]:
                
                #debugg
                #print("before swap: " + str(self.elements))
                
                self.elements[parent], self.elements[n] = self.elements[n], self.elements[parent]
                
                #debugg
                #print("after swap: " + str(self.elements))
                
                self.heapify(parent)
            else:
                return
            
    def __str__(self):
        return str(self.elements)
