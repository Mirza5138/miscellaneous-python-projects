#Took this code from the presentations to test it. 
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1) # Sort the whole list 

def quickSortHelper(lst, first, last):
    if last > first: # Base case: stop if 0 or 1 element
        pivotIndex = partition(lst, first, last) # pivot's final index
        quickSortHelper(lst, first, pivotIndex - 1) #sort left side
        quickSortHelper(lst, pivotIndex + 1, last) #sort right side

def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    quickSort(lst)
    for v in lst:
        print(v, end = " ")

def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low: # Continue until pointers cross
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1 # Move low right to check the next element

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1 # Move high left to check the previous element

        # Swap two misplaced elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]
    
# Move `high` to the correct position for the pivot
    while high > first and lst[high] >= pivot: #find an element < pivot
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first # Pivot stays at the first index

main()