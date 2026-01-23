#Took this code from the COM1001 lecture slides to test it.
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1) #quickSort is simply a specific occasion of quickSortHelper.

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last) #Returns a new index to divide the list again while sorting* the divided list.
        quickSortHelper(lst, first, pivotIndex - 1) #Sort the new divided list.
        quickSortHelper(lst, pivotIndex + 1, last)

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    quickSort(lst)
    for v in lst:
        print(v, end = " ")

def partition(lst, first, last):
    pivot = lst[first]  #Picks the first element as the pivot. This can be any arbitrary value in the given list.
    low = first + 1 #Starts the index from 2nd element of the divided list since first element the is pivot.
    high = last

    while high > low: #Continue until pointers cross.
        while low <= high and lst[low] <= pivot: #Forward search to find elements greater than the pivot.
            low += 1
            
        while low <= high and lst[high] > pivot: #Backward search to find elements smaller than the pivot.
            high -= 1

        if high > low: #Swap the two misplaced elements if indexes haven't crossed yet.
            lst[high], lst[low] = lst[low], lst[high]
    
    while high > first and lst[high] >= pivot: #Find the correct place for pivot to be placed in.
        high -= 1

    if pivot > lst[high]: #Place pivot in its correct index in the list.
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first

main()
