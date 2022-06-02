def pageCount(n, p):
  return min(p//2, n//2 - p//2) 
  #p//2 for start to that page count
  #n//2 for end to first page count and then -p//2 for removing the start to that page count