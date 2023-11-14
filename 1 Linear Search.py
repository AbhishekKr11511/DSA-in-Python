# This is linear search which goes to each element one by one

array = [2,4,7,1,3,5,10,8,28,40,15,25]

def linearSearch(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i

item = int(input("Enter your element : "))

result = linearSearch(array, item)

if(result == -1):
    print('Your item {} was not found.'.format(item))
else:
    print("Your item {} was found at index {}".format(item, result))
    
    

# Time complexity = O(n)
# Best case  = Ω(1)