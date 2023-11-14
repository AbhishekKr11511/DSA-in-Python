def prevGreaterEle(arr):
    greaterElements = ['-']
    for i in range(1,len(arr)):
        j = i-1
        while j >= 0:
            if j==0 and arr[j]<arr[i]:
                greaterElements.append('-')
                break
            elif arr[j]<arr[i]:
                j-=1
                continue
            elif arr[j]>arr[i]:
                greaterElements.append((arr[j]))
                j-=1
                break
    return greaterElements

result = prevGreaterEle([12,10,20,22,15,14,18,32,20,22,19])
print(result)

