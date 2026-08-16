class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        def check(count):
            if count[1] == 0:
                return False

            count[1] -= 1
            moves = 1 + min(count[1], count[2]) * 2 + count[0]

            if count[1] > count[2]:
                count[1] -= 1
                moves += 1

            return moves % 2 == 1 and count[1] != count[2]

        # Alice can start with either remainder 1 or remainder 2.
        return check(count[:]) or check([count[0], count[2], count[1]])