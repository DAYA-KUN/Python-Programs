def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        swapped=True
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

    return arr

arr=[8,4,6,3,9,2,7,1]
res=bubble_sort(arr)
print(res)