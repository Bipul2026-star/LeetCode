class Solution:
    def reverseDegree(self, s: str) -> int:
        i=1
        sum=0
        for ch in s:
            val=abs(ord(ch)-123)
            sum+=val*i
            i+=1
        return (sum)