def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		seen = [False] * V
		
		def dfs(node, parent):
		    seen[node] = True
		    
		    for child in adj[node]:
		        if child == parent:
		            continue
		        if seen[child]:
		            return True
		        if dfs(child, node):
		            return True
		            
		    return False
		    
        for i in range(V):
    	    if seen[i]:
    	        continue
		    if dfs(i, V):
		        return True
		    
        return False
