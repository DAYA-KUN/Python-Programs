def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return-1

arr=[10,5,6,7,4,2,8]
arr.sort()
print(arr)
target=4
result=binary_search(arr,target)

if result != -1:
    print(f"The element is found in the index of {result}")
else:
    print("The element is not found in the array")