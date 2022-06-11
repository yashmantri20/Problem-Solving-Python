def zAlgorithm(s, p, n, m):
    # Write your code here
    # Return an integer.
    string2 = len(p)
    count = 0
    for i in range(len(s)):
        if s[i:string2 + i] == p:
            count += 1
    return count
        