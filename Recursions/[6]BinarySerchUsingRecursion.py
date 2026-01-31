def recsearch(a, val, l, h):
   
    if l <= h:
        
        mid = (l + h)//2
            
        if val == a[mid]:
            return mid
            
        if a[mid] < val:
            return recsearch(a, val, mid+1, h)
        return recsearch(a, val, l, mid-1)
    return False