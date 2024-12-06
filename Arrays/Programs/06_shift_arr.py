def shift_arr(arr):
    n = len(arr)
    if n <= 1:  
        return arr
    return arr[-k:] + arr[:-k]
arr = [1, 2, 3, 4, 5,6,7]
k = 2
print(shift_arr(arr))
