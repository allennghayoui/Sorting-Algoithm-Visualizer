import time

def InsertionSort(sortingArray, createRectangles, timeInterval):
    for i in range(1, len(sortingArray)):
        tmp = sortingArray[i]

        j = i - 1

        while j >= 0 and tmp < sortingArray[j]:
            sortingArray[j + 1] = sortingArray[j]
            j -= 1

            createRectangles(sortingArray, ['red' if x == j else 'white' for x in range(len(sortingArray))])
            time.sleep(timeInterval)

        sortingArray[j + 1] = tmp

        


