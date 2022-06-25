class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        for i in nums1:
            if i in nums2 and i not in temp:
                temp.append(i)
        return temp