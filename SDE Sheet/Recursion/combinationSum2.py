class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def helper(candidates, target, path, res):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                if i >= 1 and candidates[i] == candidates[i-1]:
                   continue
                helper(candidates[i+1:],target-candidates[i],path+[candidates[i]],res)
        finalAns = []
        helper(candidates, target,[],finalAns)
        return finalAns
    