# For Binary Search the array or any Data Structure must be sorted

array = [1, 2, 3, 4, 5, 7, 8, 10, 15, 25, 28, 40]
length = len(array)

def binarySearch(item, start,  end):
    if array[(start+end)//2] == item:
        return (start+end)//2
    elif array[(start+end)//2] > item:
        return binarySearch(item, start, (start+end)//2)
    elif array[(start+end)//2] < item:
        return binarySearch(item,(start+end)//2, end)


def binarySearch2(arr, key, n): #key is the element to be found , n is the length of the array
    left = 0
    right = n-1
    while(left<=right):
        mid = (left+right)//2
        if(key>arr[mid]):
            left = mid+1
        elif(key<arr[mid]):
            right = mid-1
        else:
            return mid
    
    return -1
    

search = int(input("Enter Your Element : "))
print(binarySearch(search, 0 , length))

print(binarySearch2(array, search, length))


