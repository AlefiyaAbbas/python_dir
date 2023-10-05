'''
Radix Sorting Algorithm is a comparison-based sorting algorithm that sorts an array of numbers 
by repeatedly sorting the digits of each number in a stable way. 
Radix sort is a fast sorting algorithm with a time complexity of O(n*k), 
where n is the number of elements in the array and k is the number of digits in the largest element.
'''

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0 to 9 possible digits

    # Count occurrences of each digit in the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Calculate cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in sorted order
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
