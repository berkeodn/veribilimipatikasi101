def rev(l):
    
    l = list(reversed(l))
    neww_l = []
    
    for i in range(len(l)):

        neww_l.append(list(reversed(l[i])))
            
    return neww_l
        
l = [[1, 2], [3, 4], [5, 6, 7]]
print(rev(l))
