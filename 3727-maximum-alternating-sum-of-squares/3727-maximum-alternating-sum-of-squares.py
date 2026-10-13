class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        nums.sort(key=abs)
        for i in range(n):
            if i<n//2:
                ans-=nums[i]**2
            else:
                ans+=nums[i]**2
        return ans