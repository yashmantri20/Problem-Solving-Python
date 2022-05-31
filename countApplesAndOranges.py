def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple = 0
    orange = 0
    for i in apples:
        if a + i >= s and a + i <= t:
            apple += 1
    
    for i in oranges:
        if b + i >= s and b + i <= t:
            orange += 1
    print(apple)
    print(orange)