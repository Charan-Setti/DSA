def subarrays(n):
    c = []
    for i in range(len(n)):
        for j in range(i, len(n)):
            subarray = n[i:j + 1]
            c.append(subarray)  
    return c
n = [1, 2, 3]
print(subarrays(n))
