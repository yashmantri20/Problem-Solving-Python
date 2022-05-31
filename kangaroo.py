def kangaroo(x1, v1, x2, v2):
    # Write your code here
    a = x1 - x2
    b = v2 - v1
    if b == 0: return "NO"
    if a % b == 0 and a // b > 0: return "YES"
    else: return "NO" 