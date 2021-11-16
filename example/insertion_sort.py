def insertionsort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [12, 11, 13, 5, 6]
insertionsort(arr)
for i in range (0, len(arr)):
    print("{}".format(arr[i]), end = ' ')

print()