def is_armstrong(num):
    # Convert the number to a string to easily extract digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return total == num

# Input from user
number = int(input("Enter a number: "))

# Check and print if it's an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
