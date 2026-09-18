class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Build valid intervals
        for i in range(n):
            idx = ord(s[i]) - ord('a')

            # Only start from first occurrence
            if i != first[idx]:
                continue

            start = i
            end = last[idx]

            j = start

            while j <= end:
                curr = ord(s[j]) - ord('a')

                # Character occurs before our start
                if first[curr] < start:
                    break

                end = max(end, last[curr])
                j += 1

            else:
                intervals.append((start, end))

        # Earliest ending interval first
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans