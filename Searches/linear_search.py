def linear_search(arr,target):
    for index,value in enumerate(arr):
        if value == target:
            return index
        
    return -1

arr=[10,5,6,7,4,2,8]
target=4
result=linear_search(arr,target)

if result != -1:
    print(f"The element is found in the index of {result}")
else:
    print("The element is not found in the array")