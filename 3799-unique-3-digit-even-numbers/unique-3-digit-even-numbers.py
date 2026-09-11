class Solution:
    def totalNumbers(self, digits):
        nums = set()
        n = len(digits)

        for i in range(n):
            if digits[i] % 2 != 0:
                continue

            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    if digits[k] == 0:
                        continue

                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    nums.add(num)

        return len(nums)