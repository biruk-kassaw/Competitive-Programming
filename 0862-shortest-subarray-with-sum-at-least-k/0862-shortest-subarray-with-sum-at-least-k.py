class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        queue = deque()
        prefixes = [0]
        
        for i,num in enumerate(nums):
            prefixes.append(prefixes[i] + num)
            
        for i, prefix in enumerate(prefixes):
            
            while queue and prefix - prefixes[queue[0]] >= k:
                min_length = min(min_length, i-queue[0])
                queue.popleft()
            
            while queue and prefix < prefixes[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            
        return min_length if min_length != float("inf") else -1