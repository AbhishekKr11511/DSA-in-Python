# Take a pivot element and transfer all the elements which are less than it in left side and more than it to right side.
# Do this recursively until one element array presents and return that as is as base case

array = [5,9,8,1,2,6,4,0,7,3]
array2 = [11,22,33,44]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    leftArr = []
    rightArr = []
    pivot = arr[0]
    length = len(arr)
    for i in range(1, length):
        if pivot>=arr[i]:
            leftArr.append(arr[i])
        else:
            rightArr.append(arr[i])
    return (quickSort(leftArr) + [pivot]+ quickSort(rightArr))

result = quickSort(array)
print(result)

