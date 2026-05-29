class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            x = str(i)
            y = list(map(int, x.strip()))
            result.append(sum(y))
        return min(result)