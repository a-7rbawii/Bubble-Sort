def bubbleSort2D(myList):
    for x in range(0, len(myList)):
        for y in range(0, len(myList) - 1):
            for z in range(0, len(myList) - y - 1):
                if myList[x, z] > myList[x, z+1]:
                #for descending order, swap the ">" sign with a "<" sign 
                    temp = myList[x, z+1]
                    myList[x, z+1] = myList[x, z]
                    myList[x, z] = temp


