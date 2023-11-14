# Basic idea is, Pick an element and then insert it at the appropriate position in ascending or descending order

array = [5,9,8,1,2,6,4,0,7,3]
length = len(array)

def insertionSort(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        for j in range(i, 0, -1):
            count += 1
            if arr[j-1]>arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else: 
                break
    print(count)

insertionSort(array)
print(array)

# count = n(n-1)/2

# Time complexity = O(n^2) 
