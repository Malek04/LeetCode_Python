class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        op = []
        i = 0

        for num in range (1 , n+1):
            op.append("Push")
            if num == target[i]:
                i+=1
                if(i==len(target)):
                    break
            else:
                op.append("Pop")
        return op
