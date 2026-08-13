class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Node:
        # (left_char, right_char, length, prefix, suffix, best)
        tree = [None] * (4 * n)

        def merge(left, right):
            lc, lrc, llen, lp, ls, lb = left
            rlc, rc, rlen, rp, rs, rb = right

            length = llen + rlen

            # Start with the best answer from either side
            best = max(lb, rb)

            prefix = lp
            suffix = rs

            # Can connect the suffix of left with
            # the prefix of right
            if lrc == rlc:
                best = max(best, ls + rp)

                # Entire left segment is the same character
                if lp == llen:
                    prefix = llen + rp

                # Entire right segment is the same character
                if rs == rlen:
                    suffix = ls + rlen

            return (lc, rc, length, prefix, suffix, best)

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for idx, char in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][5])

        return ans
        return ans