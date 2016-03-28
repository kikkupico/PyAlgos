def combine_sorted(items1, items2):
    combined=[]
    i,j = 0,0
    
    while(i<len(items1) and j <len(items2)):
        if items1[i] <= items2[j]:
            combined.append(items1[i])
            i+=1
        else:
            combined.append(items2[j])
            j+=1
            
    if i<len(items1):
        combined.extend(items1[i:])
    if j<len(items2):
        combined.extend(items2[j:])
    
    #debug
    #print("{0} + {1} = {2}".format(items1,items2, combined))
    
    return combined

def merge_sort(items):
    n = len(items)
    if n <= 1:
        return items
        
    left = items[0:(int(n/2))]
    right = items[(int(n/2)):n]
    
    #debug
    #print("left:{0},right{1}".format(left,right))
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    return combine_sorted(sorted_left,sorted_right)
