
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            pos += size
            tree[pos] = value

            pos //= 2
            while pos:
                tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def find_first(node, left, right, start):
            if right <= start or tree[node] == 0:
                return -1

            if left == right - 1:
                return left

            mid = (left + right) // 2

            result = find_first(node * 2, left, mid, start)

            if result != -1:
                return result

            return find_first(node * 2 + 1, mid, right, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                end, server = heapq.heappop(busy)
                update(server, 1)

            preferred = i % k

            server = find_first(1, 0, size, preferred)

            if server == -1:
                server = find_first(1, 0, size, 0)

            if server == -1 or server >= k:
                continue

            update(server, 0)

            heapq.heappush(busy, (time + load[i], server))
            count[server] += 1

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
