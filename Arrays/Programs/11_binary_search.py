def sort(n):
    for i in range(len(n)):
        for j in range(i,len(n)):
            if n[i]>n[j]:
                n[i],n[j] = n[j],n[i]
    return n
def search(n):
    k = []
    n = sort(n)
    m = len(n)//2
    if target>n[m]:
        for i in range(m,len(n)):
            if n[i] == target:
                k.append(i)
                break
    elif target < n[m]:  
        for i in range(0, m + 1):
            if n[i] == target:
                k.append(i)
                break  
    else: 
        k.append(m)
    return k if k else "Element not in the array"
n = [5,2,4,1,3]
target = 4
print(n)
print(sort(n))
print(search(n))