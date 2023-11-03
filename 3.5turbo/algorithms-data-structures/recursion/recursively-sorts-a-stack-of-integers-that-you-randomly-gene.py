def merge_sort(stack):
    if len(stack) > 1:
        mid = len(stack) // 2
        left_stack = stack[:mid]
        right_stack = stack[mid:]

        merge_sort(left_stack)
        merge_sort(right_stack)

        # Merge sorted left and right stacks
        i = j = k = 0
        while i < len(left_stack) and j < len(right_stack):
            if left_stack[i] < right_stack[j]:
                stack[k] = left_stack[i]
                i += 1
            else:
                stack[k] = right_stack[j]
                j += 1
            k += 1

        # Copy remaining elements from left stack
        while i < len(left_stack):
            stack[k] = left_stack[i]
            i += 1
            k += 1

        # Copy remaining elements from right stack
        while j < len(right_stack):
            stack[k] = right_stack[j]
            j += 1
            k += 1

def main():
    import random

    # Generate a stack of random integers
    stack = [random.randint(1, 100) for _ in range(10)]
    print("Original Stack:", stack)

    # Sort the stack using merge sort
    merge_sort(stack)
    print("Sorted Stack:", stack)

if __name__ == "__main__":
    main()
