class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        r1 = []

        cost.sort(reverse=True)

        for i in range(len(cost)):
            if i % 3 != 2:
                r1.append(cost[i])

        return sum(r1)
