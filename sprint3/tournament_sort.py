import math
import random

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

arraySize = int(input("Choose an array size:"))
list = []
for i in range(arraySize):
    list.append(random.randint(0, 99))

sorted = tournament_sort(list)
print(list)
print(sorted)

