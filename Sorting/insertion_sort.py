def insertion_sort(arr):
    l=len(arr)
    for i in range(1,l):
        temp=arr[i]
        j=i-1
        
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=temp
    
    return arr

# Example usage
data = [12, 11, 13, 5, 6]
print("Insertion Sort:", insertion_sort(data))



