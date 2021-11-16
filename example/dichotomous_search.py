def d_search(arr, left, right, target):
    while left <= right:
        mid = int((right - left) / 2 + left)
        if arr[mid] == target:
            print('元素在数组中的索引为：{0}'.format(mid))
            break
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


arr = [ 2, 3, 4, 10, 40 ] 
x = 10
d_search(arr,0, len(arr)-1, x)