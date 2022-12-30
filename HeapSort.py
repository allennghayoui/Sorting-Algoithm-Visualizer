import time

def HeapSort(sortingArray, createRectangles, timeInterval):
    HeapSortImplementation(sortingArray, createRectangles, timeInterval)


def Heapify(sortingArray, length, i, createRectangles, timeInterval):
    largest = i

    left = i * 2 + 1
    right = i * 2 + 2

    createRectangles(sortingArray, ["blue" if i >= left and i <= right else 'white' for i in range(len(sortingArray))])
    time.sleep(timeInterval)

    if left < length and sortingArray[largest] < sortingArray[left]:
        largest = left


    if right < length and sortingArray[largest] < sortingArray[right]:
        largest = right

    if largest != i:
        sortingArray[i], sortingArray[largest] = sortingArray[largest], sortingArray[i]

        createRectangles(sortingArray, ['red' if x == largest else 'white' for x in range(len(sortingArray))])
        time.sleep(timeInterval)

        Heapify(sortingArray, length, largest, createRectangles, timeInterval)


def HeapSortImplementation(sortingArray, createRectangles, timeInterval):

    for i in range(len(sortingArray) // 2 - 1, - 1, -1):
        Heapify(sortingArray, len(sortingArray), i, createRectangles, timeInterval)

    for i in range(len(sortingArray) - 1, 0, -1):
        sortingArray[i], sortingArray[0] = sortingArray[0], sortingArray[i]
        Heapify(sortingArray, i, 0, createRectangles, timeInterval)

