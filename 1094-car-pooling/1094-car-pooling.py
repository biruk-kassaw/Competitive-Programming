class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        positions = 1001 * [0]
        for trip in trips:
            passengers = trip[0]
            start = trip[1]
            end = trip[2]
            
            positions[start] += passengers
            positions[end] -= passengers
            
        running_sum = 0
        for i in range(len(positions)):
            running_sum += positions[i]
            if running_sum > capacity:
                return False
            
        return True