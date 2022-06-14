class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        temp = {}
        for i in range(len(nums2) - 1):
            j = i + 1
            while j < len(nums2):
                if nums2[i] < nums2[j]:
                    temp[nums2[i]] = nums2[j]
                    break
                j += 1
        for i in nums1:
            if i in temp:
                ans.append(temp[i])
            else:
                ans.append(-1)
        return ans
        