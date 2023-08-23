class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = [i for i in range(k)]
        busy = []
        res = defaultdict(int)
        for i, s in enumerate(arrival):
            while busy and busy[0][0] <= s:
                heappush(available, i + (heappop(busy)[1]-i) % k)
            if available:
                j = heappop(available)%k
                res[j] += 1
                heappush(busy,(s+load[i], j))
        busiest = max(res.values())
        return [i for i in res if res[i] == busiest ]