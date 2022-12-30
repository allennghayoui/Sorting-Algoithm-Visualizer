import time

def ShellSort(sortingArray, createRectangles, timeInterval):
    gap = len(sortingArray) // 2

    while gap > 0:
        j=gap

        while j < len(sortingArray):
            i = j - gap

            while i >= 0:

                if sortingArray[i + gap] > sortingArray[i]:
                    break

                else:
                    sortingArray[i + gap], sortingArray[i] = sortingArray[i], sortingArray[i + gap]
                    
                    createRectangles(sortingArray, ['red' if x == j else 'white' for x in range(len(sortingArray))])
                    time.sleep(timeInterval)

                i = i - gap
            
            j = j + 1
        
        gap = gap // 2        


