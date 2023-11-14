def largestHisto(arr):
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

def largestArea(arr):
    maxAreas = []
    dummy= [0,0,0,0]
    for i in range(len(myArray)):
        for j in range(len(myArray)):
            if myArray[i][j] == 0:
                dummy[j] = 0
            dummy[j]=dummy[j]+myArray[i][j]
        # print(dummy)
        maxAreas.append(largestHisto(dummy))
    print(max(maxAreas))


myArray = [ [0,1,1,0],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,0,0]]

largestArea(myArray)