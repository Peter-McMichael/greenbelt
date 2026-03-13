import cProfile
import multiprocessing
import random
import time


# merge sort
def merge(arr, l, m, r):
    numOfLeftElements = m - l + 1
    numOfRightElements = r - m
#comment
    leftArray = [0] * numOfLeftElements
    rightArray = [0] * numOfRightElements


    for i in range(numOfLeftElements):
        leftArray[i] = arr[l + i]

    for j in range(numOfRightElements):
        rightArray[j] = arr[m+1+j]


    i = 0
    j = 0
    k = l


    while i < numOfLeftElements and j < numOfRightElements:
        if leftArray[i] <= rightArray[j]:
            arr[k] = leftArray[i]
            i+=1
        else:
            arr[k] = rightArray[j]
            j+=1
        k+=1
    while i < numOfLeftElements:
        arr[k] = leftArray[i]
        i+=1
        k+=1

    while j < numOfRightElements:
        arr[k] = rightArray[j]
        j+=1
        k+=1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)

        merge(arr, l, m, r)



# quick sott

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


def mergeFunction(arr):
    local = arr.copy()

    start = time.perf_counter()

    pr = cProfile.Profile()
    pr.enable()
    mergeSort(local, 0, len(local) - 1)
    pr.disable()
    end = time.perf_counter()

    print(f"merge sort time: {end - start:.4f} seconds")
    pr.print_stats()


def quickFunction(arr):
    local = arr.copy()

    start = time.perf_counter()

    pr = cProfile.Profile()
    pr.enable()
    quickSort(local, 0, len(local) - 1)
    pr.disable()
    end = time.perf_counter()

    print(f"quick sort time: {end - start:.4f} seconds")
    pr.print_stats()

if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(7234)]
    
    p1 = multiprocessing.Process(target=mergeFunction, args=(arr,))
    p2 = multiprocessing.Process(target =quickFunction, args=(arr,))

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()

    print(f"Total elapsed time: {end_time - start_time:.4f} seconds.")


