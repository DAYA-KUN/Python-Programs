def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k) # Output is 2, Even if try has return, only finally returns