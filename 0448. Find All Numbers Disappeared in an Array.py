class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (n+1)
        for num in nums:
            result[num] += 1
        
        l = []

        for i in range(1,n+1):
            if result[i]==0:
                l.append(i)

        return l

        
        
