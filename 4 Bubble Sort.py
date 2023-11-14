# The Basic Idea is the take the greatest elelement of the array,
# And put it at the end of the array, as the array starts being sorted from the end of the array

array = [5,9,8,1,2,6,4,0,7,3]
length = len(array)


def bubbleSort(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            count += 1
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(count)

bubbleSort(array)

print(array)

# The count will be O(n(n-1)/2)

# Time complexity = O(n^2)