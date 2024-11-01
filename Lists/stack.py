stack=[1,2,3,4,5,6,7]

stack.append(8) #push

stack.pop() #pop

p=stack[-1] #peek - Top element

def is_empty(): #isempty
    if stack:
        print("Stack is not empty")
    else:
        print("Stack is empty")

