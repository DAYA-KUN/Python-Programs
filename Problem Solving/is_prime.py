def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            
    return True

print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(12))
print(is_prime(9))