import time
def partition(array, low, high):

    # Choosing the rightmost element as pivot
    # In this case, the worst case cenario for ordering 
    # is if the rightmost element is always in place
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse all elements and compare each one with pivot
    for j in range (low, high):
        if array[j] <= pivot:
            # If the element found is smaller than the pivot
            # swap it with the greater element pointed by i
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
        
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i+1])

    # Return the position from where partition is done
    return i + 1

def quicksort(array, low, high):
    if low < high:
        
        # Find pivot element
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pivot = partition(array, low, high)

        # Recursive call on the left and right of pivot
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)
        
        # Worst case scenario time complexity is O(N²)
        # Average case is O(N log N)
        # Auxiliary space: O(log N)

def quicksortListComprehension(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x< pivot]
        right = [x for x in arr[1:] if x> pivot]
        return quicksortListComprehension(left) + [pivot] + quicksortListComprehension(right)
    # Time complexity is O(n log n)
    # auxiliary space is O(n)

def binary_search(arr, key):
    comparison_count = 0
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        time.sleep(0.000000001)
        middle = (begin + end)//2
        if arr[middle] == key:
            comparison_count += 1
            return [middle, comparison_count]
        elif arr[middle] > key:
            comparison_count += 1
            end = middle - 1
        else:
            comparison_count += 2
            begin = middle + 1
    return [-1, comparison_count]
    # Time complexity is O(log N)
    # Auxiliary space is O(1)

def sequentialSearch(arr, key):
    begin = 0
    while begin < len(arr):
        time.sleep(0.000000001)
        if arr[begin] == key:
            return [begin, begin+1]
        else:
            begin += 1
    return [-1, begin]
    # Time complexity is O(N)
    # Auxiliary space is O(1)

def optimizedSequentialSearch(arr, key):
    # This implementation uses Hash table to map each element to its position
    hash_table = {}
    for i in range(len(arr)):
        time.sleep(0.000000001)
        hash_table[arr[i]] = i
    # Search for element in the hash table
    if key in hash_table:
        return [hash_table[key], 1]
    else:
        return [-1, 1]
    
    # Time complexity is O(N)
    # Auxiliary space is O(N?)