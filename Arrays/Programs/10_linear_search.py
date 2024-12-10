def search(n):
    k = []
    for i in range(len(n)):
        if c == n[i]:
            k.append(i+1)
        
    return k if k else "Element not in array"
n = [34,2,24,3,1,5,3,3,6,7,54,8,3,3]
c = 34
print(search(n))