class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
			
        prev = timeSeries[0] 
        poison = duration 
        
        for i in range(1,len(timeSeries)): 
            
            if prev + duration >= timeSeries[i]: 
                overlap = prev + duration -timeSeries[i] 
                poison += duration-overlap
            else:
                poison += duration
                
            prev = timeSeries[i]
        return poison  