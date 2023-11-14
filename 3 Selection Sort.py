# The Basic idea is to find the minimum element by traversing through the array
# And putting it at the beginning. Then increasing the index, as the array starts to be
# Sorted from the beginning

array = [5,9,8,1,2,6,4,0,7,3]
length = len(array)

def selectionSort(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if(arr[min]>arr[j]):
                min = j
        arr[i],arr[min] = arr[min],arr[i]

selectionSort(array)
print(array)

# The Count will be = n(n-1)/2, where n is the length of the array
