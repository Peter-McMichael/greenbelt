import math
import random
import cProfile
import time
import pstats

def selection_sort(arr):
    for i in range (0, len(arr)):
        min_index = i
        for j in range (i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def tournament_sort(arr):
    if not arr:
        return []
    
    players = [(value, i) for i, value in enumerate(arr)]
    #create tuples

    n=len(players)

    size = 1

    while size < n:
        size *= 2

    INF = (math.inf, math.inf)

    tree = [INF] * (2*size)

    for i in range(n): # put numbers in tree
        tree[size + i] = players[i]

    for i in range(size -1, 0, -1):
        left_child = tree[2*i]
        right_child = tree[2*i+1]
        tree[i] = min(left_child, right_child)

    result = []

    for _ in range (n):
        winner = tree[1]
        result.append(winner[0]) #add lowest number to results.

        leaf_index = size + winner[1]
        tree[leaf_index] = INF
        leaf_index //= 2

        while leaf_index >= 1:
            left_child = tree[2*leaf_index]
            right_child = tree[2*leaf_index + 1]
            tree[leaf_index] = min(left_child, right_child)

            leaf_index //= 2
    return result

   
def profile_tournament_sort(arr):
    local = arr.copy()


    profiler = cProfile.Profile()
    start = time.perf_counter()


    profiler.enable()
    result = tournament_sort(local)
    profiler.disable()


    end = time.perf_counter()


    print("\n--- Tournament Sort ---")
    print("Sorted correctly:", result == sorted(arr))
    print(f"Time: {end - start:.6f} seconds")


    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative").print_stats(10)




def profile_selection_sort(arr):
    local = arr.copy()


    profiler = cProfile.Profile()
    start = time.perf_counter()


    profiler.enable()
    result = selection_sort(local)
    profiler.disable()


    end = time.perf_counter()


    print("\n--- Selection Sort ---")
    print("Sorted correctly:", result == sorted(arr))
    print(f"Time: {end - start:.6f} seconds")


    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative").print_stats(10)




def main():
    size = int(input("Enter array size: "))
    arr = [random.randint(0, 99) for _ in range(size)]


    print("\nOriginal array:")
    print(arr)


    profile_tournament_sort(arr)
    profile_selection_sort(arr)
    start = time.perf_counter()
    tournament_sort(arr.copy())
    end = time.perf_counter()
    print("Tournament sort:", end - start)


    start = time.perf_counter()
    selection_sort(arr.copy())
    end = time.perf_counter()
    print("Selection sort:", end - start)




if __name__ == "__main__":
    main()

