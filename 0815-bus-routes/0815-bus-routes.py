class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        
        graph = defaultdict(list)
        for i, bus in enumerate(routes):
            for route in bus:
                graph[route].append(i)
        q = deque([(source, 0)])
        
        visited_bus = set()
        visited_routes = set()
        
        while q:
            route, route_len = q.popleft()
            if route == target:
                return route_len
            for bus in graph[route]:
                
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    
                    for new_route in routes[bus]:
                        if new_route not in visited_routes:
                            visited_routes.add(new_route)
                            q.append((new_route, route_len + 1))
                            
        return -1
            