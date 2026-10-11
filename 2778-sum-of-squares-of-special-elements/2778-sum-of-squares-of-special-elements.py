class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            j=i+1
            if n%j==0:
                s+=nums[i]**2
        return(s)
       