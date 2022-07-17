class Solution:
    def rob(self, arr: List[int]) -> int:
        incl = 0
        excl = 0

        for i in arr:
            new_excl = max(excl, incl)

            incl = excl + i
            excl = new_excl

        return max(excl , incl)