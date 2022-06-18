class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp = []
        temp1 = []
        for i in set(nums1):
            if i not in nums2:
                temp.append(i)
        for i in set(nums2):
            if i not in nums1:
                temp1.append(i)
        return [temp,temp1]