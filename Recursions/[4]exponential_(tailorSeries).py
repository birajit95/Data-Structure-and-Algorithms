def exp(x, n, s=1):
    if n == 0:
        return s
        
    s = (x/n)*s + 1
    return exp(x, n - 1, s)

print(exp(2, 3))
