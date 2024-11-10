#Using an empty string

string = "hello"
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("Original String:", string)
print("Reversed String:", reversed_string)


#Using recursion

def reverse_string(s):

    if len(s)<=1:
        return s
    
    return reverse_string(s[1:])+s[0]

print("Reversed String:", reverse_string(string))