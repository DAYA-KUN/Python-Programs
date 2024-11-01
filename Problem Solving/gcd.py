def gcd(n1,n2):
    while n2:
        n1,n2=n2,n1%n2

    return n1

print(gcd(2,10))
print(gcd(50,225))

