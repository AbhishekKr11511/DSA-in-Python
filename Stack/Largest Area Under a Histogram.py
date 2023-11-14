def largestArea(arr):
    areas = []
    for i in range(len(arr)):
        count = 1
        j=i+1
        k=i-1
        while j<len(arr) and arr[j]>=arr[i]:
            count+=1
            j+=1
        while k>=0 and arr[k]>=arr[i]:
            count+=1
            k-=1
        areas.append(arr[i]*count)
    return max(areas)

print(largestArea([12,2,5,4,1,7,8]))