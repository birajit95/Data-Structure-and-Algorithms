def binary_search(a, val):
    
    n = len(a)
    low = 0
    high = n-1
    
    
    while low <= high:
        mid = (low + high)// 2
        
        if a[mid] == val:
            return mid
        
        if a[mid] < val:
            low = mid + 1
            
        
        else:
            high = mid - 1
            
        
            
    return False