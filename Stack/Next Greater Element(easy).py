def nextGreaterEle(arr):
    greaterArr = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j == len(arr)-1 and arr[i]>arr[j]:
                greaterArr.append('-')
            if arr[i]<arr[j]:
                greaterArr.append(arr[j])
                break
    
    # Since there is no loop for the last element, as there are no more elements to compare we append one more '-'
    greaterArr.append('-')
    return greaterArr

print(nextGreaterEle([30, 50, 20, 15, 25]))