class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sub = 0
        maxim = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                sub += 1
                if sub > maxim:
                    maxim = sub
            else :
                sub = 0
        return maxim
