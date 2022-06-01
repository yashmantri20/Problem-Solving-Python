def migratoryBirds(arr):
    # Write your code here
    a = {}
    for i in range(len(arr)):
        if arr[i] not in a:
            a[arr[i]] = 1
        else: 
            a[arr[i]] += 1
    maxVal = 0
    ans = 0
    for i in a:
        if a[i] >= maxVal:
            if maxVal == a[i] and ans < i:
                continue
            maxVal = a[i]
            ans = i
    return ans