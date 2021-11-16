def reversearr(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def leftrotate(arr, num):
    n = len(arr)
    reversearr(arr, 0, num - 1)
    reversearr(arr, num, n-1)
    reversearr(arr, 0, n - 1)

def printarr(arr):
    for i in range (0, len(arr)):
        print(arr[i], end = ' ')

arr = [1, 2, 3, 4, 5, 6, 7]
leftrotate(arr, 3)
printarr(arr)
print()