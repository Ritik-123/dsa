import math

# Linear Search

def linearSearch(array, value):
    """
    Used to return the index value of target value.
    """
    
    for i in range(len(array)):
        if array[i] == value:
            return i
        
    return -1

# array= [10,4,25,67,43]
# print(linearSearch(array, 25))


# Binary Search

def binarySearch(array, value):
    """
    Used to return the index value of target value.
    """
    
    start= 0
    end= len(array)-1
    middle= math.floor((start + end)/ 2)

    while (value != array[middle]) and start <= end:

        if value > array[middle]:
            start= middle + 1
        else:
            end= middle - 1

        middle= math.floor((start + end)/ 2)
        print(start, middle, end)

    if value == array[middle]:
        return middle
    else:
        return -1
    
array= [10, 20, 30, 40, 50, 60, 70, 80]
print(binarySearch(array, 70))