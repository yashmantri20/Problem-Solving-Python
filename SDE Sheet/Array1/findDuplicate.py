class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #with extra space
        temp = {}
        for i in nums:
            if i in temp:
                return i
            else:
                temp[i] = 1
        #tortoise and hare
        #two pointers one is slow and one is fast, we will increment slow by 1 and fast by 2

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        