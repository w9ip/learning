def alternate(A):
    for v in A:
        for x in A:
            if v < x:
                break
        else:
            return v
        
    return None

print(alternate([1, 5, 2, 9, 3, 4]))
      
