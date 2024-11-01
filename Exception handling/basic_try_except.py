try:
    n=int(input("Enter a number:"))
    res=10//n
    print(res)

except ZeroDivisionError:
    print("Cannot divide by Zero!")

    