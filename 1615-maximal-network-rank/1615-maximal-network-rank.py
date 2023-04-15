class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        city = defaultdict(list)
        for edge in roads:
            city[edge[0]].append(edge[1])
            city[edge[1]].append(edge[0])

        max_rank = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                is_connected = 1 if j in city[i] else 0
                num_connect = len(city[i]) + len(city[j]) - is_connected
                
                if num_connect > max_rank:
                    max_rank = num_connect
        
        return max_rank