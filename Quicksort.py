#Originally, learnt this version of quicksort (middle pointer pivot):

def quicksort1(L, low, high):
    if low < high:
        pos = split(L, low, high)
        
        quicksort1(L, low, pos - 1)
        quicksort1(L, pos + 1, high)
        
def split(L, low, high):
    mid = (low + high) // 2
    pivot = L[mid]
    
    L[mid], L[low] = L[low], L[mid]
    left = low + 1
    right = high
    
    while left <= right:
        while left <= right and L[left] < pivot:
            left += 1
        
        while L[right] > pivot:
            right -= 1
        
        if left < right:
            L[left], L[right] = L[right], L[left]
        
    L[low], L[right] = L[right], L[low]
    
    return right


L = [5,9,4,13,37,21,10,33]
if __name__ == "__main__":
    quicksort1(L, 0, len(L) - 1)
    print(L, "with lengthier quicksort")


#But actually quicksort can be also condensed into this using list comprehension:

def quicksort2(mainList):
    length = len(mainList)
    if length <= 1:
        return mainList
    
    else:
        pivot = mainList[0]
        greater = [element for element in mainList[1:] if element > pivot]
        lesser = [element for element in mainList[1:] if element <= pivot]
        return quicksort2(lesser) + [pivot] + quicksort2(greater)
    

mainList = [5,9,4,13,37,21,10,33]
if __name__ == "__main__":
    print(quicksort2(mainList), "with shorter quicksort")