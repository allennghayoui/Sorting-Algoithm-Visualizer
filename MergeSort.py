import time

def MergeSort(sortingArray, createRectangles, timeInterval):
    ImplementMergeSort(sortingArray, 0, len(sortingArray) - 1, createRectangles, timeInterval)

def ImplementMergeSort(sortingArray, left, right, createRectangles, timeInterval):
    if left < right:
        mid = (left + right)//2
        ImplementMergeSort(sortingArray, left, mid, createRectangles, timeInterval)
        ImplementMergeSort(sortingArray, mid + 1, right, createRectangles, timeInterval)
        Merge(sortingArray, left, mid, right, createRectangles, timeInterval)


def Merge(sortingArray, left, mid, right, createRectangles, timeInterval):
    createRectangles(sortingArray, Colors(len(sortingArray), left, mid, right))
    time.sleep(timeInterval)

    leftArray = sortingArray[left:mid+1]
    rightArray = sortingArray[mid+1:right+1]

    leftIndex = 0
    rightIndex = 0

    for index in range(left, right + 1):
        if leftIndex < len(leftArray) and rightIndex < len(rightArray):
            if leftArray[leftIndex] <= rightArray[rightIndex]:
                sortingArray[index] = leftArray[leftIndex]
                leftIndex += 1
            else:
                sortingArray[index] = rightArray[rightIndex]
                rightIndex += 1

        elif leftIndex < len(leftArray):
            sortingArray[index] = leftArray[leftIndex]
            leftIndex += 1
        else:
            sortingArray[index] = rightArray[rightIndex]
            rightIndex += 1

    createRectangles(sortingArray, ["blue" if i >= left and i <= right else 'white' for i in range(len(sortingArray))])
    time.sleep(timeInterval)
        



def Colors(length, left, mid, right):
    colors = []

    for index in range(length):
        if index >= left and index <= right:
            if index <= mid:
                colors.append("blue")
            else:
                colors.append("red")
        else:
            colors.append("white")
    return colors