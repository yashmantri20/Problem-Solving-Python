class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        temp = []
        temp1 = []
        pivotArr = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                temp.append(nums[i])
            elif nums[i] == pivot:
                pivotArr.append(pivot)
            else:
                temp1.append(nums[i])
        return temp1 + pivotArr + temp
        