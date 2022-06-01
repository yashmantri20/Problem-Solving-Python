def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(len(s)):
        a = s[i:i+m]
        if(sum(a) == d and len(a) == m):
            count += 1
    return count