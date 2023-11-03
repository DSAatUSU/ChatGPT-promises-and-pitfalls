import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

# Generate a random array of numbers
arr = [random.randint(0, 100) for _ in range(10)]

# Sort the array using quicksort
sorted_arr = quicksort(arr)

print("Sorted array:", sorted_arr)
print("Sorting algorithm used: Quicksort")