def duplicates(n):
    c = []
    for i in n:
        if i not in c:
            c.append(i)
    return c
n = [1,2,3,4,5,6,7,1,2,3,4,56,7,3,3,3,3,2]
print(duplicates(n))