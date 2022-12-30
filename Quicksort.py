import time

def Quicksort(sortingArray, createRectangles, timeInterval):
    QuicksortImplementation(sortingArray, 0, len(sortingArray) - 1, createRectangles, timeInterval)

def partition(sortingArray, low, high, createRectangles, timeInterval):
    border = low

    createRectangles(sortingArray, Colors(len(sortingArray), low, high, border, border))
    time.sleep(timeInterval)

    pivot = sortingArray[high]

    greaterIndex = low - 1

    for j in range(low, high):
        if sortingArray[j] <= pivot:
            createRectangles(sortingArray, Colors(len(sortingArray), low, high, border, j, True))
            time.sleep(timeInterval)
            greaterIndex += 1

            sortingArray[greaterIndex], sortingArray[j] = sortingArray[j], sortingArray[greaterIndex]

        createRectangles(sortingArray, Colors(len(sortingArray), low, high, border, j))
        time.sleep(timeInterval)

    createRectangles(sortingArray, Colors(len(sortingArray), low, high, border, high, True))
    time.sleep(timeInterval)

    sortingArray[greaterIndex + 1], sortingArray[high] = sortingArray[high], sortingArray[greaterIndex + 1]

    return greaterIndex + 1


def QuicksortImplementation(sortingArray, low, high, createRectangles, timeInterval):
    if low < high:

        partitionIndex = partition(sortingArray, low, high, createRectangles, timeInterval)

        QuicksortImplementation(sortingArray, partitionIndex + 1, high, createRectangles, timeInterval)

        QuicksortImplementation(sortingArray, low, partitionIndex - 1, createRectangles, timeInterval)



def Colors(length, low, high, border, current, swapping=False):
    colors = []

    for index in range(length):
        if index >= low and index <= high:
                colors.append("blue")
        else:
            colors.append("white")
    if index == high:
        colors[index] = "yellow"
    elif index == border:
        colors[index] = "red"
    elif index == current:
        colors[index] = "gray"
    if swapping:
        if index == border or index == current:
            colors[index] = "green"
    return colors