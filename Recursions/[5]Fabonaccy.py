def febo(n, memo = {0:0, 1:1}):
    if n in memo:
        return memo[n]
    
    memo[n] = febo(n-1, memo) + febo(n-2, memo)
    return memo[n]
    
print(febo(6))