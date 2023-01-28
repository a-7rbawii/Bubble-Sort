def bubbleSort(myList):
    for j in range(0, len(myList)):
        for i in range(0, len(myList)-1):
            if myList[i] > myList[i+1]:
            #for descending order, swap the ">" sign with a "<" sign
                temp = myList[i+1]
                myList[i+1] = myList[i]
                myList[i] = temp

myList = [99, 5, -11, 0, 1, 33, 555]

print("Unsorted array --> {}".format(myList))

bubbleSort(myList)

print("Sorted array --> {}".format(myList))