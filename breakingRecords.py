def breakingRecords(scores):
    minVal = scores[0]
    maxVal = scores[0]
    minValCount = 0
    maxValCount = 0
    for i in scores:
        if i > maxVal:
            maxVal = i
            maxValCount += 1
        if i < minVal:
            minVal = i
            minValCount += 1
    return [maxValCount, minValCount]