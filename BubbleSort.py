import time


def BubbleSort(sortingArray, createRectangles, timeInterval):
    for i in range(len(sortingArray)):
        for j in range(len(sortingArray) - i - 1):
            if sortingArray[j+1] < sortingArray[j]:
                sortingArray[j], sortingArray[j + 1] = sortingArray[j + 1], sortingArray[j]
                createRectangles(sortingArray, ['red' if x == j else 'white' for x in range(len(sortingArray))])
                time.sleep(timeInterval)