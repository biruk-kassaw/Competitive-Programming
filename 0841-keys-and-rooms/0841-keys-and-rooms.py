class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([rooms[0]])
        visited = set()
        visited.add(0)
        while queue:
            n = len(queue)
            
            for i in range(n):
                room = queue.popleft()
                for j in room:
                    if j in visited:
                        continue
                    visited.add(j)
                    queue.append(rooms[j])
        return len(visited) == len(rooms)