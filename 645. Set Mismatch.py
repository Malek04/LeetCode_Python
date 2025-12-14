class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        value = [0] * (n + 1)
        duplicate, miss = 0, 0

        for num in nums:
            value[num] += 1

        for i in range(1, n + 1): 
            if value[i] == 2:
                duplicate = i
            if value[i] == 0:
                miss = i

        return [duplicate, miss]
