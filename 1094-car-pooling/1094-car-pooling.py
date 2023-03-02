class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        positions = 1001 * [0]
        for trip in trips:
            passengers = trip[0]
            start = trip[1]
            end = trip[2]
            
            positions[start] += passengers
            positions[end] -= passengers
            
        prefix = [0]   
        for i in range(1,len(positions)):
            prefix.append(prefix[i-1] + positions[i-1])
            if prefix[i] > capacity:
                return False
            
        return True