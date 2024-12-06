def shift_zeros(arr):
    n = len(arr)
    if n <= 1:  
        return arr
    non_zero_index = 0
    for i in range(n):
        if arr[i]!=0:
            arr[non_zero_index]=arr[i]
            print(arr)
            non_zero_index+=1
    for i in range(non_zero_index,n):
        arr[i]=0
    return arr
arr = [1, 0, 2, 0, 3, 0, 4]
print(shift_zeros(arr))  
