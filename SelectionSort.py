import time

def SelectionSort(sortingArray, createRectangles, timeInterval):
    
    for i in range(len(sortingArray)):
        smallest = i

        for j in range(i + 1, len(sortingArray)):
            if sortingArray[smallest] > sortingArray[j]:
                smallest = j
                createRectangles(sortingArray, ['red' if x == j else 'white' for x in range(len(sortingArray))])
                time.sleep(timeInterval)
        sortingArray[i], sortingArray[smallest] = sortingArray[smallest], sortingArray[i]

        