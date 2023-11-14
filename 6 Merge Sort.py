# Basic Idea = 


array2 = [5,9,8,1,2,6,4,0,7,3]
array = [10, 23, 45, 7, 18, 32, 5, 14, 27, 39]
length = len(array)

def mergeSplit(arr):
    if len(arr)==1:
        return arr
    n = len(arr)
    firstHalf = arr[0:n//2]
    secondHalf = arr[n//2:n]
    return mergeBoth(mergeSplit(firstHalf), mergeSplit(secondHalf))

def mergeBoth(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    i = 0
    j = 0
    mergedArray = []
    while j<b or i<a:
        if i==a:
            mergedArray.append(arr2[j])
            j+=1
        elif j==b:
            mergedArray.append(arr1[i])
            i+=1
        elif(arr1[i]<arr2[j]):
            mergedArray.append(arr1[i])
            i+=1
        elif(arr1[i]>arr2[j]):
            mergedArray.append(arr2[j])
            j+=1
    return mergedArray

result = mergeSplit(array)
print(result)


# Time complexity is = O(nlog(n))
