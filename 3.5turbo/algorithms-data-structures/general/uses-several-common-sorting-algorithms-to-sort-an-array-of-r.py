import random
import time

# Function to generate a random array of numbers
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to check if an array is sorted
def is_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))

# Bubble Sort algorithm
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Insertion Sort algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

# Merge Sort algorithm
def merge_sort(array):   
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    
    merged.extend(left[l:])
    merged.extend(right[r:])
    
    return merged

# Quick Sort algorithm
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure the time taken by a sorting algorithm
def measure_time(sort_function, array):
    start_time = time.time()
    sorted_array = sort_function(array)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, sorted_array

# Main function
def main():
    # Generate a random array of numbers
    array_size = 1000
    array = generate_random_array(array_size)

    # Perform sorting and measure time
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    for algorithm_name, sort_function in sorting_algorithms.items():
        execution_time, sorted_array = measure_time(sort_function, array.copy())
        print(f"{algorithm_name}: Execution Time = {execution_time:.6f}s, Sorted Array = {sorted_array[:10]}...")
        
        # Verify if the array is sorted correctly
        if not is_sorted(sorted_array):
            print("Sorting failed!")

if __name__ == "__main__":
    main()
