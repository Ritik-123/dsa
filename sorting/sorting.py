import math


# 1. Bubble Sort.

def bubbleSort(mylist):
    """
    Ascending order.
    """
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - i - 1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1]= mylist[j+1], mylist[j]
    print(mylist)

# customList= [1,10,8,5,7,3,2,4,6,9]
# bubbleSort(customList)


def bubbleSortdesc(mylist):
    """
    Descending order.
    """
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - i - 1):
            if mylist[j] < mylist[j+1]:
                mylist[j], mylist[j+1]= mylist[j+1], mylist[j]
    print(mylist)

# customList= [1,10,8,5,7,3,2,4,6,9]
# bubbleSortdesc(customList)


# 2. Selection Sort

def selectionSort(mylist):
    """
    Ascending order.
    """
    for i in range(len(mylist)):
        min_index= i
        for j in range(i+1, len(mylist)):
            if mylist[min_index] > mylist[j]:
                min_index= j
        mylist[i], mylist[min_index]= mylist[min_index], mylist[i]
    print(mylist)

# customList= [1,10,8,5,7,3,2,4,6,9]
# selectionSort(customList)


# 3. Insertion Sort

def insertionSort(mylist):
    """
    Ascending Order
    """
    for i in range(1, len(mylist)):
        key= mylist[i]
        j= i - 1

        while j>=0 and key<mylist[j]:
            mylist[j+1]= mylist[j]
            j -= 1

        mylist[j+1]= key
    
    print(mylist)

# customList= [1,10,8,5,7,3,2,4,6,9]
# insertionSort(customList)

def bucketSort(mylist):
    """
    Ascending Order
    """
    numberOfBuckets= round(math.sqrt(len(mylist)))
    maxValue= max(mylist)
    arr= []

    # Create number of buckets
    for _ in range(numberOfBuckets):
        arr.append([])

    for i in mylist:
        index_b= math.ceil(i * numberOfBuckets / maxValue)
        arr[index_b - 1].append(i)

    for j in range(numberOfBuckets):
        arr[j]= insertionSort(arr[j])

    k= 0
    
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            mylist[k]= arr[i][j]
            k += 1
    
    return mylist

customList= [1,10,8,5,7,3,2,4,6,9]
bucketSort(customList)

# Bucket Sort with negative numbers.
def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
    
    buckets = [[] for _ in range(numberofBuckets)]
    
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array