def divisibleSumPairs(n, k, ar):
    count = 0
    i = 0
    j = 0
    while(i < len(ar)):
        a = ar[i]
        b = ar[j+1]
        j += 1
        if (a + b) % k == 0 and i < j:
            count += 1
        if j == len(ar) - 1:
            j = i            
            i += 1
    return count