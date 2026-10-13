class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Replace each element with its square
        nums = [x * x for x in nums]
        
        # Sort squares in ascending order
        nums.sort()
        
        n = len(nums)
        m = n // 2
        
        # Subtract the smaller half, add the larger half
        ans = 0
        for i in range(m):
            ans -= nums[i]
        for i in range(m, n):
            ans += nums[i]
            
        return ans