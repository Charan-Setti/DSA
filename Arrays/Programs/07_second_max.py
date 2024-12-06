arr = [3,2,5,4,7,8,4,2]
maxx = arr[0]
for i in range(len(arr)):
    if maxx<arr[i]:
        maxx = arr[i]
print(arr)
arr.remove(maxx)
maxx2 = arr[0]
for i in range(len(arr)):
    if maxx2<arr[i]:
        maxx2 = arr[i]
print(maxx2)