import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        hq = []

        for n in nums:
            heapq.heappush(hq, (-1 * n, n))


        for i in range(k):
            max_value = heapq.heappop(hq)

            res += max_value[1]

            divided_value = ceil(max_value[1] / 3)

            heapq.heappush(hq, (-1 * divided_value, divided_value))

        return res
        