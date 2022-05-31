# O(n*2)
def getTotalX(a, b):
    min = a[-1]
    max = b[0]
    ans = []
    for i in range(min, max + 1):
        flag = True
        for j in a:
            if(i % j != 0):
                flag = False
        if flag: ans.append(i)
    count = 0
    for i in ans:
        flag = True        
        for j in b:
            if j % i != 0: flag = False
        if flag: count += 1
    return count