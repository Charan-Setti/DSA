def missing():
    n=arr[len(arr)-1]
    r=[]
    m = []
    for i in range(1,n+1):
        r.append(i)
    for i in range(n):
        if r[i] not in arr:
            m.append(r[i])
    return m
arr = [1,2,3,5,6,8,9,10,15]
print(missing())

