from tkinter import *
from tkinter import ttk
import random
import BubbleSort
import MergeSort
import Quicksort
import InsertionSort
import SelectionSort
import ShellSort
import HeapSort




class UserInterface:
    def __init__(self, parent, width, height, timeInterval):
        self.parent = parent
        self.width = width
        self.height = height
        self.timeInterval = timeInterval

        self.sortingArray = []
        #self.numbersArray = self.CreateNumberArray()
        self.SetupInterface()

        
        self.ComboBoxValues = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Shell Sort", "Heap Sort", "Merge Sort", "Quicksort"]

        self.sortingAlgorithmVar = StringVar()

        self.sortingAlgorithmsComboBox = ttk.Combobox(self.parent, value=self.ComboBoxValues, textvariable=self.sortingAlgorithmVar)        
        self.sortingAlgorithmsComboBox.grid(row=0, column=0, sticky='W')

        self.sortButton = ttk.Button(self.parent, text="Sort", command=lambda:self.Sort(self.sortingAlgorithmVar.get(), self.sortingArray))
        self.sortButton.grid(row=0, column=0)

        self.resetButton = ttk.Button(self.parent, text="Reset", command=lambda:self.SetupInterface())
        self.resetButton.grid(row = 0, column = 0, sticky="E")

    
    def SetupInterface(self):
        self.sortingArray = self.CreateNumberArray()
        frame = self.CreateFrame()
        self.CreateCanvas(frame)
        self.InitialDrawing(self.sortingArray)


    def CreateFrame(self):
        self.frame = ttk.Frame(self.parent, padding=10)
        self.frame.grid()


    def CreateCanvas(self, parent):
        self.canvas = Canvas(parent, width=self.width, height=self.height, background='white')
        self.canvas.grid(column=0, row=1, sticky=(N,W,E,S))


    def CreateNumberArray(self):
        NUMBER_OF_RECTANGLES = 10
        MIN_HEIGHT = 0
        MAX_HEIGHT = 400
        numbersArray = []
        for i in range (NUMBER_OF_RECTANGLES):
            numbersArray.append(random.randint(MIN_HEIGHT, MAX_HEIGHT))
        return numbersArray


    def CreateRectangles(self, numbersArray, color):
        self.canvas.delete("all")
        START_X_PADDING = 6
        CANVAS_BOTTOM = 550
        for index, height in enumerate(numbersArray):
            start_x = self.GetStartingX(index) + START_X_PADDING
            end_x = self.GetEndingX(start_x)
            start_y = self.height - height
            end_y = CANVAS_BOTTOM
            self.canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color[index], width=1, outline='black')
            self.canvas.create_text(start_x + 10, start_y, anchor=SW, text=str(numbersArray[index]))
        self.parent.update_idletasks()
    

    def InitialDrawing(self, sortingArray):
        COLOR = ['red' for i in range(len(sortingArray))]
        self.CreateRectangles(sortingArray, COLOR)


    def GetStartingX(self, index):
        return index * 50
    

    def GetEndingX(self, start_x):
        return start_x + 40

    
    def Sort(self, sortingAlgorithm, sortingArray):
        COLOR = ['blue' for index in range(len(sortingArray))]
        if sortingAlgorithm == 'Bubble Sort':
            BubbleSort.BubbleSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Insertion Sort':
            InsertionSort.InsertionSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Selection Sort':
            SelectionSort.SelectionSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Shell Sort':
            ShellSort.ShellSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Heap Sort':
            HeapSort.HeapSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Merge Sort':
            MergeSort.MergeSort(sortingArray, self.CreateRectangles, self.timeInterval)

        elif sortingAlgorithm == 'Quicksort':
            Quicksort.Quicksort(sortingArray, self.CreateRectangles, self.timeInterval)
            

        self.CreateRectangles(sortingArray, COLOR)




def main():
        root = Tk()
        root.title("Sorting Algorithm Visualizer")
        root.iconbitmap('')
        root.geometry('500x530')
        CANVAS_WIDTH = 500
        CANVAS_HEIGHT = 500
        TIME_INTERVAL = 0.2

        # COLOR = ['blue' for index in range(len(sortingArray))]
        UI = UserInterface(root, CANVAS_WIDTH, CANVAS_HEIGHT, TIME_INTERVAL)

        root.mainloop()


if __name__ == '__main__':
    main()