class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        if nums == sorted_arr:
            return True
        else:
            for i in range(len(nums) - 1):
                x = nums.pop(0)
                nums.append(x)
                if nums == sorted_arr:
                    return True
                    break
            else:
                return False