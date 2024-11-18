def reverse_arr():
    if len(arr)<=1:
        return arr
    if len(arr)>1:
        x=[]
        for i in range(len(arr)-1,-1,-1):
            x.append(arr[i]) 
    return x
arr = [14,2,35,10,9,4,3]
print(reverse_arr())
    