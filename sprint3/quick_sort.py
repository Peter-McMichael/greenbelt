
def partition(arr, left, right):
    pivot = arr[right] #value
    left_pointer = left # index
    right_pointer = right - 1 # index

    while left_pointer <= right_pointer:
        while left_pointer <= right_pointer and arr[left_pointer] < pivot:
            #left_pointer increase
            left_pointer += 1
        while left_pointer <= right_pointer and arr[right_pointer] >= pivot:
            right_pointer -= 1

        if left_pointer <= right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1
            right_pointer += 1

        arr[left_pointer], arr[right] = arr[right], arr[left_pointer]
        return left_pointer
    
def quickSort(arr, left, right):
    if left >= right:
        return # when finished
    pivot_index = partition(arr, left, right)
    quickSort(arr, left, pivot_index - 1)
    quickSort(arr, pivot_index + 1, right)




arr = [22, 11, 88, 66, 55, 77, 33, 44]
print("Unsorted array:", arr)

quickSort(arr, 0, len(arr)-1)

print("Sorted array:", arr)