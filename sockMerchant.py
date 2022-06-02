def sockMerchant(n, arr):
    socks = {}
    for sock in arr:
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1
    pairCount = 0
    for sock in socks:
        pairCount += socks[sock] // 2  
    return pairCount  