
def pow(m,n):
    if n == 0:
        return 1
        
    return m * pow(m, n-1)
    

print(pow(2,3))

