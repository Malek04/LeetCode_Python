class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        for i in range(n):
            l.insert(i, nums[i])
            l.insert(i+ n ,nums[i])
        return l
