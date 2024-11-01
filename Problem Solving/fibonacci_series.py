def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)
    
n=9
series=[fibonacci_series(i) for i in range(n+1)]
print(series)