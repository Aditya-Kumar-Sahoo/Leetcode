class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        result = set(nums1) & set(nums2)
        if len(result) >= 1:
            return min(result)
        else:
            return -1